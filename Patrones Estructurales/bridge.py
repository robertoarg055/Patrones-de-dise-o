class Exporter:
    def export(self, content):
        pass 
class PDFExporter(Exporter):
    def export(self, content):
        print(f"Exporting {content} to PDF...")
class HTMLExporter(Exporter):
    def export(self, content):
        print(f"Exporting {content} to HTML...")
class JSONExporter(Exporter):
    def export(self, content):
        print(f"Exporting {content} to JSON...")
class Report:
    def __init__(self, data, exporter: Exporter):
        self.data = data
        self.exporter = exporter
    def generate(self):
        raise NotImplementedError("Subclases deben implementar generate()")
    def export(self):
        content = self.generate()
        self.exporter.export(content)
class UserReport(Report):
    def generate(self):
        return f"User Report{self.data}"
class SalesReport(Report):
    def generate(self):
        return f"Sales Report{self.data}"
class DataReport(Report):
    def generate(self):
        return f"Data Report{self.data}"
if __name__ == "__main__":
    report1 = UserReport("",PDFExporter())
    report2 = SalesReport("",HTMLExporter())
    report3 = DataReport("",JSONExporter())
    report1.export()
    report2.export()
    report3.export()
