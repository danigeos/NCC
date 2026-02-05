#!/usr/bin/env python3
### NCC calculator by D. Garcia-Castellanos (CSIC-Geo3BCN), 2025

import warnings
# --- SILENCE WARNINGS BEFORE OTHER IMPORTS ---
# This catches the NotOpenSSLWarning from urllib3 v2 on macOS systems with LibreSSL
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL 1.1.1+.*")
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

import pandas as pd
import numpy as np
import argparse
import requests
import sys 

# --- OpenAlex Configuration ---
OPENALEX_API_URL = "https://api.openalex.org/works"
# IMPORTANT! Replace this placeholder with your real email.
EMAIL_FOR_API = "YOURMAILHERE@gmail.com" 

# --- Calculation Functions ---

def compute_nnc(df, author_id, r):
    """
    Calculates the Normalized Number of Citations (NCC) for each publication.
    The weight formula W_i ensures the sum of contributions from all co-authors 
    of an article is always 1.
    """
    nic_list, n_list, N_list, nc_list = [], [], [], []
    
    if "Cited by" not in df.columns:
         raise ValueError("Internal error: The 'Cited by' column was not found.")
        
    for index, row in df.iterrows():
        try:
            authorships = row.get("authorships", [])
            authors_ids = [a['author']['id'].split('/')[-1] for a in authorships if a.get('author') and a['author'].get('id')]
            N = len(authors_ids)
            
            try:
                author_index = authors_ids.index(author_id)
                i = author_index + 1
            except ValueError:
                i = np.nan 
            
            NC = int(row["Cited by"]) 
            
            weight_factor = 0.0
            if N > 0 and not np.isnan(i) and NC > 0:
                if r == 1.0:
                    weight_factor = 1.0 / N
                else:
                    # Exponential normalization formula: W_i = ( (1-r) * r^(i-1) ) / (1 - r^N)
                    numerator = (1 - r) * (r ** (i - 1))
                    denominator = 1 - (r ** N)
                    if denominator != 0:
                        weight_factor = numerator / denominator
            
            NCC = NC * weight_factor
            nic_list.append(NCC)
            n_list.append(i)
            N_list.append(N)
            nc_list.append(NC)
            
        except Exception:
            nic_list.append(0)
            n_list.append(np.nan)
            N_list.append(0)
            nc_list.append(0)

    df["NC"] = nc_list
    df["n"] = n_list
    df["N"] = N_list
    df["NCC"] = nic_list
    return df

def compute_h_index(values):
    """Calculates h-index from a list/series of citations (can be float)."""
    clean_vals = [v for v in values if pd.notnull(v) and v >= 0]
    if not clean_vals:
        return 0
    clean_vals.sort(reverse=True)
    h = 0
    for i, c in enumerate(clean_vals, start=1):
        if c >= i:
            h = i
        else:
            break
    return h

def get_author_data(author_name):
    """Searches for author and downloads publications from OpenAlex."""
    if EMAIL_FOR_API == "YOURMAILHERE":
        print("\nERROR: INCOMPLETE CONFIGURATION!")
        print("Edit the script and replace 'YOURMAILHERE' with your real email to use the OpenAlex API.")
        sys.exit(1)
        
    print(f"Searching for author: '{author_name}'...")
    AUTHOR_SEARCH_BASE_URL = "https://api.openalex.org/authors"
    search_params = {"search": author_name, "mailto": EMAIL_FOR_API}
    
    author_response = requests.get(AUTHOR_SEARCH_BASE_URL, params=search_params)
    author_response.raise_for_status()
    author_data = author_response.json()

    if not author_data['results']:
        raise ValueError(f"No author found for name: {author_name}.")

    main_author = author_data['results'][0]
    author_id = main_author['id'].split('/')[-1]
    author_display_name = main_author['display_name']

    print(f"Primary author found: {author_display_name} (ID: {author_id})")

    works_list, cursor = [], '*'
    print("Downloading publications. This may take a few moments...")

    while True:
        works_params = {
            "filter": f"author.id:{author_id}",
            "select": "title,cited_by_count,authorships,publication_year",
            "per_page": 200,
            "cursor": cursor,
            "mailto": EMAIL_FOR_API
        }
        works_response = requests.get(OPENALEX_API_URL, params=works_params)
        works_response.raise_for_status()
        works_data = works_response.json()
        works_list.extend(works_data.get('results', []))
        next_cursor = works_data.get('meta', {}).get('next_cursor')
        if next_cursor:
            cursor = next_cursor
            print(f"Downloaded {len(works_list)} publications so far...")
        else:
            break
            
    print(f"Download complete. Total publications: {len(works_list)}")
    df = pd.DataFrame(works_list)
    df.rename(columns={'title': 'Title', 'cited_by_count': 'Cited by'}, inplace=True)
    return df, author_id, author_display_name

def format_authors_for_list(authorships):
    """Extracts and formats up to 3 surnames and adds 'et al.' if there are more."""
    names, MAX_NAMES = [], 3
    if not isinstance(authorships, list):
        return "Unknown"
    for auth in authorships:
        try:
            display_name = auth.get("author", {}).get("display_name")
            if not display_name: continue
            names.append(str(display_name).split()[-1])
            if len(names) >= MAX_NAMES: break
        except: continue
    if not names: return "Unknown"
    return ", ".join(names) if len(authorships) <= MAX_NAMES else f"{', '.join(names)}, et al."

def main():
    SYNTAX_EXPLAINER = (
        "\n***           Normalized Citation Count          ***"
        "\n*** NCC calculator (D. Garcia-Castellanos, 2025) ***"
        "\n***************** USAGE SYNTAX *********************"
        '\n./normalized_citation_count.py "Author Name" [--weight_ratio <value>] [--save]'
        '\nExample: ./normalized_citation_count.py "G.K. Gilbert" --weight_ratio 0.3 --save'
        '\nweight_ratio is the relative weight attributed to consecutive authors.'
        '\nThe total weight given to a citation is always 1, decreasing-exponentially distributed among authors.'
        '\nCount weights for N authors and weight_ratio = .5:'
        '\n\tN = 1: weight = 1'
        '\n\tN = 2, weights: 2/3 + 1/3 = 1'
        '\n\tN = 3, weights: 4/7 + 2/7 + 1/7 = 1'
        '\n\tN = inf, weights: 1/2 + 1/4 + 1/8 + ... = 1'
        '\nFor weight_ratio = .333'
        '\n\tN = 1, weight = 1'
        '\n\tN = 2, weights = 3/4 + 1/4 = 1'
        '\n\tN = 3, weights = 9/13 + 3/13 + 1/13 = 1'
        '\n\tN = 4, weights = 27/40 + 9/40 + 3/40 + 1/40 = 1'
        '\nMeaning: If weight_ratio is 1/3 and there are 4 authors, they receive credit in a proportion of 27, 9, 3, 1'
        '\n--save: Writes full results to a CSV file (Default: No)'
        "\n*****************************************************"
        '\n'
    )
    
    parser = argparse.ArgumentParser(
        description="NCC (Normalized Number of Citations) Calculator using OpenAlex data.",
        formatter_class=argparse.RawTextHelpFormatter 
    )
    parser.add_argument("author_name", type=str, help="Full author name to search.")
    parser.add_argument("--weight_ratio", type=float, default=0.5, help="Weight ratio (r) between consecutive authors.")
    parser.add_argument("--save", action="store_true", help="Save results to CSV automatically.")
    args = parser.parse_args()

    AUTHOR_WIDTH, TITLE_WIDTH, TOP_N = 30, 20, 30
    R_VALUE = args.weight_ratio

    print(SYNTAX_EXPLAINER)
    try:
        df_raw, author_id, author_name = get_author_data(args.author_name)
        df_result = compute_nnc(df_raw.copy(), author_id, R_VALUE)
        df_result['Author List'] = df_result['authorships'].apply(format_authors_for_list)
        
        last_df_result = df_result[df_result["NCC"] > 0][["Author List", "publication_year", "Title", "Cited by", "n", "N", "NCC"]].sort_values(by="NCC", ascending=False)
        
        if not last_df_result.empty:
            print(f"\n--- Results per publication (Top {TOP_N} with NCC > 0) ---")
            separator_length = AUTHOR_WIDTH + 4 + TITLE_WIDTH + 5 + 5 + 10
            print(f"{'Authors (Surnames)':<{AUTHOR_WIDTH}} | {'Year':<4} | {'Title':<{TITLE_WIDTH}} | {'NC':<5} | {'NCC':<5}")
            print("-" * separator_length)

            for _, row in last_df_result.head(TOP_N).iterrows():
                author_list = row['Author List'][:AUTHOR_WIDTH].ljust(AUTHOR_WIDTH)
                year = str(row['publication_year']).ljust(4)
                title = row['Title'][:TITLE_WIDTH].ljust(TITLE_WIDTH)
                nc = str(row['Cited by']).ljust(5)
                nnc = f"{row['NCC']:.1f}".ljust(5) 
                print(f"{author_list} | {year} | {title} | {nc} | {nnc}")

            should_save = args.save
            if not should_save:
                choice = input(f"\nWould you like to save the results to a CSV file? (y/n, default n): ").lower()
                if choice == 'y': should_save = True

            if should_save:
                filename = f"{author_name.replace(' ', '_')}_nnc_results.csv"
                last_df_result.to_csv(filename, index=False)
                print(f"\nResults saved to: {filename}")
        else:
             print("\nNo NCC could be calculated for any publication.")
        
        total_nc = df_result["NC"].sum()
        total_nnc = df_result["NCC"].sum()
        h_index_nc = compute_h_index(df_result["NC"].tolist())
        h_index_nnc = compute_h_index(df_result["NCC"].tolist())
        
        print("\n" + "="*52)
        print(f"| {'NCC SUMMARY':^48} |")
        print("="*52)
        print(f"| Author: {author_name:<40} |")
        print(f"| OpenAlex ID: {author_id:<35} |")
        print(f"| Weight Ratio (r): {R_VALUE:<30} |") 
        print(f"|              classic      weighted               |")
        print(f"| citations:   {total_nc:<12} {total_nnc:.1f} <--- Normalized Citation Count ")
        print(f"| h-index:     {h_index_nc:<12} {h_index_nnc:<22} |")
        print("="*52 + "\n")

    except Exception as e:
        print(f"\n[ERROR] {e}")

if __name__ == "__main__":
    main()