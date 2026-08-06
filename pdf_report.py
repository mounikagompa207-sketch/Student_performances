from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(student_name,
                 result,
                 score,
                 risk,
                 confidence):

    filename = f"{student_name}_Report.pdf"

    doc = SimpleDocTemplate(filename, pagesize=letter)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Student Performance Report</b>", styles["Title"]))

    story.append(Paragraph(f"Student : {student_name}", styles["BodyText"]))

    story.append(Paragraph(f"Prediction : {result}", styles["BodyText"]))

    story.append(Paragraph(f"Performance Score : {score}", styles["BodyText"]))

    story.append(Paragraph(f"Risk Level : {risk}", styles["BodyText"]))

    story.append(Paragraph(f"Prediction Confidence : {confidence}%", styles["BodyText"]))

    doc.build(story)

    return filename