# ☕ Coffee Revenue Intelligence
### Product Optimization & Revenue Analysis — Afficionado Coffee Roasters

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.2-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

---

## 📌 What is this project?
A complete end-to-end data analysis project that analyzes **1,49,116 real coffee shop transactions** to identify which products drive revenue, which are underperforming, and how the business can optimize its menu for higher profitability.

---

## 🎯 Business Problem
Afficionado Coffee Roasters had no clear visibility into:
- Which products are popular vs profitable
- Which products could be removed without revenue loss
- How dependent the business is on specific categories

---

## 📊 Key Findings
| Metric | Value |
|---|---|
| Total Revenue | ₹ 6,98,812 |
| Total Transactions | 1,49,116 |
| Unique Products | 80 |
| Top Category | Coffee (38.6%) |
| Hero Products | 42 out of 80 drive 80% revenue |
| Highest Revenue Product | Sustainably Grown Organic Lg (₹21,151) |
| Lowest Revenue Product | Dark Chocolate regular (₹755) |

---

## 💡 Key Insights
1. **Coffee + Tea = 66.7% of revenue** — high category dependency
2. **Popularity ≠ Profitability** — most sold product (Earl Grey Rg) is NOT the highest revenue product
3. **38 products contribute only 20% of revenue** — menu simplification opportunity
4. **Large size variants always outperform** small/regular sizes

---

## 🛠️ Tools & Technologies
| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and manipulation |
| Matplotlib | Charts and visualizations |
| Streamlit | Interactive web dashboard |
| GitHub | Version control |

---

## 📁 Project Files
| File | Description |
|---|---|
| `analysis.py` | Data loading, cleaning, revenue analysis, Pareto |
| `charts.py` | Static chart generation (bar, pie, scatter) |
| `dashboard.py` | Interactive Streamlit web dashboard |
| `research_paper.docx` | Detailed EDA report with findings |
| `executive_summary.docx` | 1-page summary for stakeholders |

---

## 🚀 How to Run

### Install dependencies:
```bash
pip install pandas matplotlib streamlit
```

### Run the dashboard:
```bash
python -m streamlit run dashboard.py
```

---

## 📈 Dashboard Features
- ✅ KPI cards — Revenue, Transactions, Products
- ✅ Category and Store Location filters
- ✅ Top-N product slider (5 to 20)
- ✅ Revenue by category bar chart
- ✅ Top N products chart
- ✅ Revenue share pie chart
- ✅ Bottom 10 products chart
- ✅ Product performance table
- ✅ Popularity vs Revenue scatter plot

---

## 👩‍💻 Author
**Shruti Mahawar**
GitHub: [@ShrutiMahawar06](https://github.com/ShrutiMahawar06)

