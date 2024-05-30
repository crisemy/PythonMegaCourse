from fpdf import FPDF
import pandas

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()

    def available(self):
        in_stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        return in_stock

    # Decreases the quantity of products by Article
    def decrease(self):
        df.loc[df['id'] == self.id, 'in stock'] -= 1
        df.to_csv("articles.csv", index=False)
        

class Receipt:
    def __init__(self, article):
        self.article = article
    
    # Defines and generates the PDF file which in this case is a billing file
    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")

# Prints out the content of the articles.csv file
print(df)
# Init the article class
article_ID = input("Choose an article to buy: ")
article = Article(article_id=article_ID)
if article.available(): # Meaning that it has stock
    article.decrease()
    receipt = Receipt(article) # Decrease method to update the File
    receipt.generate()
    print(f"Purchased {article.name}. Stock decreased by 1.")
else:
    print("No such article in stock.")
