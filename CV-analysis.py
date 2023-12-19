import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF Library


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text


def analyze_skills(cv_text, target_skills):
    vectorizer = CountVectorizer().fit_transform([cv_text] + target_skills)
    vectors = vectorizer.toarray()
    similarity_matrix = cosine_similarity(vectors)
    similarity_to_cv = similarity_matrix[0, 1:]
    return similarity_to_cv


def process_cvs_in_folder(folder_path, target_skills):
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            cv_path = os.path.join(folder_path, filename)

            cv_text = extract_text_from_pdf(cv_path)
            similarity_scores = analyze_skills(cv_text, target_skills)

            # Add if CV analysis results are not empty
            if any(similarity_scores):
                data.append({"Filename": filename, **dict(zip(target_skills, similarity_scores))})

    return data


def main():
    # Path to the folder containing CV's
    cv_folder_path = "cv.dır"


    target_skills = [
        "Python",
        "Machine Learning",
        "Data Analysis",
        "Communication",
        # You can add other skills
    ]

    # Process Resumes
    results = process_cvs_in_folder(cv_folder_path, target_skills)

    if not results:
        print("Analysis results not found.")
        return

    # Convert the results to a DataFrame and save to Excel file
    excel_filename = "cv_analysis_results.xlsx"
    df = pd.DataFrame(results, columns=["Filename"] + target_skills)
    df = df.sort_values(by=target_skills, ascending=False)
    df.to_excel(excel_filename, index=False)

    print(f"Results saved to Excel file: {excel_filename}")


if __name__ == "__main__":
    main()
