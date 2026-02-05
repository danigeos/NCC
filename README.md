# **Normalized Citation Count (NCC)**

A credit-conservative approach to prevent the inflation of scientific publishing.

## **The Problem: Author Inflation in Science**

In the current bibliometric landscape, citations are typically treated as "free" resources. When a paper with 50 authors receives one citation, the scientific community often credits each of those 50 authors with a full citation in their respective h-index and total citation counts.

This system has created problematic incentives:

* **Exponential Growth of Authorship:** There is a strategic advantage to adding more co-authors, as it multiplies the "bibliographic impact" of a single paper without increasing actual scientific value.

* **Dilution of Merit:** It becomes difficult to distinguish between a researcher who led a study and one who provided minor peripheral input.

* **Hyper-authorship:** We now see "mega-papers" with hundreds or even thousands of authors, which distorts traditional metrics of productivity.

## **The Solution: Normalized Citation Count (NCC)**

The **Normalized Citation Count (NCC)** proposes a "zero-sum" approach to scientific credit. Its core principle is simple: **Every citation to a scientific publication counts as exactly one unit of credit to be split among the co-authors.**

### **How it Works**

Instead of rewarding every author with 100% of the credit, the NCC distributes the credit based on the author's position and the total number of contributors.

* **Normalization to 1:** The sum of the contributions (NNC) of all co-authors for a single article is always equal to 1.

* **Positional Weighting:** Using a **Weight Ratio (**$r$**)**, the system assigns more credit to primary authors while still acknowledging the contributions of co-authors.

### **Benefits to the Scientific Community**

* The impact of a citation in the evaluation system is not multiplied by the number of coauthors.

* **Fairer Impact Assessment:** NCC provides a more realistic view of a researcher's individual contribution to the field.

* **Discouraging "Gift" Authorship:** When authors must "share" citation credit, there is less incentive to add names that did not contribute significantly.

* **Correcting the h-index:** The NNC allows calculating a **Normalized h-index**, which provides a more rigorous measure of influence resistant to author-inflation.

* **Correcting the current underestimation of early stage researchers who concentrate the burden of publishing but not the credit of citations**.

* While the following script assumes an exponential decrease in the weight attributed to each author according to her/his position in the author list, deviations from this dominant pattern could be easily implemented if publishers collected the relative contributions from the authors.

## **Technical Details**

The script uses a series of $N$ terms ($N$ being the number of authors) which adds to 1. Each term is then used to calculate the weight ($W$) of each author at position $i$ in a paper with $N$ total authors:

$$
W_i = \frac{(1-r) \cdot r^{i-1}}{1 - r^N}
$$

Where $r$ is the **Weight Ratio**.

* Note: If $r = 1.0$, the script defaults to equal distribution ($1/N$).

* If $r < 1.0$, the credit decreases exponentially for authors further down the list.

### **Numerical Examples**

**Example:** `./normalized_citation_count.py "G.K. Gilbert" --weight_ratio 0.3 --save`

The weight ratio is the relative weight attributed to consecutive authors. The total weight given to a citation is always 1, geometrically distributed among authors.

**Weights for** $N$ **authors and** $r = 0.5$**:**

* $N = 1$: weight = 1

* $N = 2$: weights: $2/3 + 1/3 = 1$

* $N = 3$: weights: $4/7 + 2/7 + 1/7 = 1$

* $N = \infty$: weights: $1/2 + 1/4 + 1/8 + \dots = 1$

**Weights for** $r = 0.333$**:**

* $N = 1$: weight = 1

* $N = 2$: weights = $3/4 + 1/4 = 1$

* $N = 3$: weights = $9/13 + 3/13 + 1/13 = 1$

* $N = 4$: weights = $27/40 + 9/40 + 3/40 + 1/40 = 1$

*Meaning: For weight_ratio = 1/3 and 4 authors, they get credit in a proportion of 27, 9, 3, 1.*

## **NNC Python Calculator: Installation & Setup**

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/yourusername/ncc-calculator.git](https://github.com/yourusername/ncc-calculator.git)
   cd ncc-calculator
