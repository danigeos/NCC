# **Normalized Citation Count (NCC)**

A credit-conservative approach to prevent the inflation of scientific publishing.

## **The Problem: Author Inflation in Science**

In the current bibliometric landscape, citations are typically treated as "free" resources. When a paper with 50 authors receives one citation, the scientific community often credits each of those 50 authors with a full citation in their respective h-index and total citation counts.

This system has created a perverse incentive:

* **Exponential Growth of Authorship:** There is a strategic advantage to adding more co-authors, as it multiplies the "bibliographic impact" of a single paper without increasing actual scientific output.  
* **Dilution of Merit:** It becomes difficult to distinguish between a researcher who led a study and one who provided minor peripheral input.  
* **Hyper-authorship:** We now see "mega-papers" with hundreds or even thousands of authors, which distorts traditional metrics of productivity.

## **The Solution: Normalized Citation Count (NCC)**

The **Normalized Citation Count (NCC)** proposes a "zero-sum" approach to scientific credit. Its core principle is simple: **Every citation to a scientific publication counts as exactly one unit of credit, shared among the co-authors.**

### **How it Works**

Instead of rewarding every author with 100% of the credit, the NCC distributes the credit based on the author's position and the total number of contributors.

* **Normalization to 1:** The sum of the contributions (NNC) of all co-authors for a single article is always equal to 1\.  
* **Positional Weighting:** Using a **Weight Ratio (![][image1])**, the system assigns more credit to primary authors while still acknowledging the contributions of co-authors.

### **Benefits to the Scientific Community**

* The impact of a citation in the evaluation system is not multiplied by the number of coauthors.  
* **Fairer Impact Assessment:** NCC provides a more realistic view of a researcher's individual contribution to the field.  
* **Discouraging "Gift" Authorship:** When authors must "share" citation credit, there is less incentive to add names that did not contribute significantly.  
* **Correcting the h-index:** The script calculates a **Normalized h-index** (h-NNC), which provides a more rigorous measure of influence resistant to author-inflation.

## **Technical Details**

The script uses an exponential normalization formula to calculate the weight (![][image2]) for an author at position ![][image3] in a paper with ![][image4] total authors:

![][image5]Where ![][image1] is the **Weight Ratio**.

* If ![][image6], the credit is split equally (![][image7]).  
* If ![][image8], the credit decreases exponentially for authors further down the list.

## **NNC Python Calculator: Installation & Setup**

1. **Clone the repository:**  
   git clone \[https://github.com/yourusername/ncc-calculator.git\](https://github.com/yourusername/ncc-calculator.git)  
   cd ncc-calculator

2. **Install dependencies:** The script requires pandas, numpy, and requests.  
   pip install pandas numpy requests

3. **Configure API Access:** Open normalized\_citation\_count.py and replace YOURMAILHERE@gmail.com with your real email address. This is required by the **OpenAlex API** to identify your requests.

## **Usage Guidelines**

Run the script from your terminal by providing the author's name in quotes.

### **Basic Command**

python3 normalized\_citation\_count.py "G.K. Gilbert"

### **Advanced Options**

* **Adjusting Weighting:** Use \--weight\_ratio to change how credit is distributed.  
  \# Give much more weight to the first author (r=0.3)  
  python3 normalized\_citation\_count.py "Albert Einstein" \--weight\_ratio 0.3

* **Saving Results:** Use the \--save flag to automatically export the detailed publication list to a CSV file.  
  python3 normalized\_citation\_count.py "Albert Einstein" \--save

### **Interactive Save**

If the \--save flag is not provided, the script will interactively ask if you wish to export the results before exiting.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAeCAYAAAAYa/93AAAApklEQVR4XmNgGAWjAC9glpeX/wjE3+Tk5JRAAkDaF8j/A8TvgVgSRTVQ4L+xsTErkL4LYgPxAQUFhVNQjfUgMbhioIQGUPAkVONpqIb7UH4wlI/QAORclJGRUYGyUSSVlZVlQXyggTFwDUiACarhG7oEVgA0JR+qoQZdDisAKnwL0qClpcWGLocVoLufICDJ/cCgjYBqKEGXwwUYgZ7OQxccBYMXAADhjDGmy3MAKgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAfCAYAAAD5h919AAABwUlEQVR4Xu1UPUvEQBQ8OBBBEAshkCLJQQo5QRAL7RSx8i8I2goHlnYi+IH4caJXaGGn9oKgveDZ2CkWaquNlYgcIgc6L9kXn8/kkussMjDs7szse7u5YwuFHDkkXNc9dhxnH1zDfBWs0hpjRWQOwA1wGVwBt8A93/e7OeN53gztw7hLNcAajexTkSrMU4xfhg3wqFQqDZhIEett8ElkHrFnJyoCoMk09BeReSZNZgJwAAX6tEfApiHOaE+CfNu2e7UeQZxkUnsE3NBKa+SGn35J67/ARXDyOe0R3PCTpjVK9CJwEfoxtQdtBHxo1Qh6nXJa/wMuAp7FeTKDgp70seyE3pBaItyff8y90hdQaN3Mg0b4vBMq82ZZVpfUEoHwlSnUVHr0qbgRGs8KbRC85nUqED7kQqzh5BcoOiYygQ9uSo3nmYCii7JRuVzuwPxDZkSjE7Nnnl4UmUkFNk/JRhhf5RNjtCb5uOWNWbd3GwI2D3MjnLIf421Mhv/i7+AlOK4zqaBngxslnRT6uch8aj8zRJGa9ghe+DIHGcx7tJ8ZXETrDHgVk7nTXlswRWIfVQJuMdrqIO2gqIUcOXL8D3wDxS+vYWyuONQAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAgCAYAAAAv8DnQAAAAuUlEQVR4XmNgGLZAXl6+1djYmBVdHAyAkt+B+L+cnNxJdDkwAEpuASlQUVFhR5ejAgAaK4ouBgZSUlJcIHuB+BiIlpWVVUZRABJEZgPxPbgk0DuxQIEeKNsXqmApXIGCgkInjA2U+AE1jRmuABlAdcOtQwFACU2QJNDEU+hyYACUfApSICMjI4QuBwboxqNYBeREgwSAvugH8YF0OdCqSLgCIMcdqkAbyBbA6lCg4F2oNf/Q5UYBEQAArVQzP6P8oAgAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAfCAYAAADjuz3zAAABZElEQVR4Xu2Tvy8EURSF11KoFApRzM/MNEqNRqlT6ERUWpJt+Ac0W2iIiG4bLImaiEbi76BRKBARUaDkm827yd27b+xmS5kvOZl95545897uTq1W8X+I43gRtdGZUztJkmmbK2B2ig6Z73Btol10YHMdCK2hfQI36MfpzeYKXO5LcqzvoyjatrkuCJ7ocjvXuNJx63txZWNSzE7ObcZR7/fgLiTMde+vXeM3ipNZ3wvHSgi/y1qKsVd1zs2eOM289b0QPKJkU9bcfFe2a59XigvXZZ3n+YQUB0EwqaJDFfd4Tg/icap11tc6V4r9foUwDJekXDw+v6RpOqdzpdB7zA1b1i9Qu+68XfohfXHhUesXMGupXY8MU1yK2vUVp7uwcy+EZ9Cn9TXMH1X5rJ17IXiJmtbXZFk2JcV21oP7xW/lBo64Yf+vmoGKecuWCX2gV/Tsrt/4CzYr8OAVMi3rV1RUDMgvrHV//VyL1KcAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAfCAYAAACvUTALAAACMklEQVR4Xu2Yv0vDUBDHpSIKDqKiRZombRrRwUGsg6A4OeokODkK/S/UXSzqIghuDm7ij0k7uKqTIDiobREUnIqLi1r9Xn2V9NpXYpNiWt4Hjtfc9+6S921amra0KBQKhUKhaAIMw0ghvnjeKaFQqJf6ReRpjUQiCV7XkGAjE9jQs22DheB1TrAsq0/0b9ly7ZTTdX3fXtuQmKaJfegL0Wg0iLXbjVno+6zUizdkg/JkJtcaFjdmFe8gRJZrMKuDNKxHXGtY3JiFnjXRe8w1Qja3FclXxBtOblIC6xyOPxA5xABv8AsuzboRvTtcIyrOpUQ8Hm/D+iAKznH7XZKGi1kpa/ARLs0q9Bm2L3c7ZXNhyjBOeCHEK1GQEcfzZQ1VQF26WF9L8HlO8Misda4RZXNxcK1pmlVJjMViYTrGBS3+NvgMj8xKco2oOreq6FO8MAufrk2uEdK5aBgVYoprfsalWbeid5drhHQukgck4ORTXHMKHhs09M/UGnyeE3R3ZiWpDzfKKdcI6Vyp8Adw0gRm7NUafJ4T3JiF7+oe0fvCNTwldMk0T8z6D5yYFQ6HR0RNnmuyXrzxq5THI9VQiYATmqLprETwLwEYMI6NTOOaT4obRixRHuuYvRgbP5SZgrtrkPLwYNmeF/Vpe64ACmdJxE+Ffq75kWAw2InrzeG6H42fH9J3iHvaHOIJ8c57kMuifpvnCeQnhTn090yGXjfVM2EdCfCEQqFQKBQKhaK+fAP7Ew+BkVS8uAAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC4AAAAfCAYAAACYn/8/AAACd0lEQVR4Xu2XvWsUQRjG4wcqChY2h8fdzR13IhxaGNHGSrC2sFIUFSzUNoU22ggRbFRMYWGnCVgIYqWIoP+ANioiKkRjIYdIUFCR+PGbu5kwPsxNdo8UW+wPHm73mWfmfXezXxkbKykpyY0x5j3arH7hoem/6nkYm0DTaMbpJvYKzVkYu4WuNRqNi/xOosvoguYWIXg9VTwFc48y9676HsbOoyn03NZwuq85C/4NtBDknjabzZOLgW63uwbzXRDoK1gjM8z73el01qqvcIAfyD7KUis1voqFjtRqtY7dybLYMLLO8zlfizN5SjMWxsbRd/WjjNo4xa8yb1L9GEHjz1L18O+gc+pHSS2UIuscDvA4uue21/l67Xa7rlnr20tZ/SijNM51vZE5C+rHIDeLdgT7/gbshTk3lr2PURon/4Szd0j9GLo2+3tjNVut1la8b6GXJLbIUuTJx7K+phk81/vwwLiNzoa5JHkbr9fru8jPqR8jvL5DzODl8l9dt706iKXRBZaCbI/mt6kfwww+B8bVt/i66IDf10ySERpflixjr31t3inb+Z3XTJI8jZM7wXX4QP1hpNZ1T6Z+bfQYTWgmSc7G/1Sr1fXqx+DaPo0eqh8SNG7rr9TxJDkbz5SzkP3CX2ef+iHcK/vz1LePnp1ojxl8ufUnsn+GZ+luM+RmYvwKZ/CS+iHuzXgYvXLr/rRfkKm3oct9Vj8Kwa9ozgy+Et+gt277I/qheYstoJ5iD47cPOqhT7Yh9Iubb5NmPYxPccDH1F8WKpXKBpPxFV8o7JOEs3JQ/cKT5TIpHPYfDhqfVb/w0PRLmt+ifuGh8RfqlZQUlH/hvuN9pteczQAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAfCAYAAACvUTALAAACsElEQVR4Xu2XO2gUURSGQ0QMWBifi/uYmX34KCQGN4WiaJtCGwUrKxEsbC1sfBR2waA2ASEQSGMnPioNJGClVoIgQU2CoCCCQZCAxkT/s3tGbv7dWWb3zhgj94PD3Tn/Pefee+bOzp2uLofD4XA4HP8Bvu9PwH6xPy65XG6rxKstSxsEwXnutybBQg5iQR+NBdaM+8WhUqls1/jbhm+D+DzPu2v2XZOUSiWswztdLBYzaDfbFAtxS81icUNuil+KydqqgUldkkmhPcZaHGyKFe4g2BxrmE+PzusBa38dLHJMt/oIa+1gUyzEDGnsQ9aEqLzr4PwKW8DgJXGgPYHrn7B52E4O6BTkmtRJXGatEyyL9Upj77AmNM0rjmq1uh7tO+0whe33XDRM5mpDQJto7mnNfZZ1GyyLVYvzjT93k4a8KMpeDPhMxRfaYVavTzUEtAFy9yL2s8Tj9yDrSZBQsW6wJjTkxcXLfD5faSaWy+WCXGNCZ/4ExEDeVohbgC3hjbWf9SRJqFjDrAkt87YUYyIFgn3DQS/PWhokUSzs+lusCZF5EdCv4gRr7RDUD4yS54ucjFlPGstivdbYUdaEyLxw3hMBgx9hrRPwKO5Gvh+w7+FjngaWxRqWONzgx6wJkXkjBUuy2ew2v378kG+uQ6zbYlMs3MQtGvuJNdzsTVFaasUK0dPyWx3nJOudEqdYhUJhn/ZZZi0qFrvtmvjxgtqzQpCDqAY9WSGkBMZ5quNdYC0m3SjAABZyFDkehQuGnRM/2gNmZyz8ftjH9AvYXbvEjxpcMf3af8b01UDH4yLiqLCDtTTBmOM6qeustSKTyWxEzDzm/d6vH6Tf+PVdOwP7AFvkGPjmvIhPK/gP6zzkr2JWfgf/wjdhMzC5i9glfexfJbrZ4XA4HA6Hw+FIl98VQg7cWXLz0wAAAABJRU5ErkJggg==>