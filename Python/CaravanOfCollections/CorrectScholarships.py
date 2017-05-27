
def correctScholarships(bestStudents, scholarships, allStudents):
    return all(x in scholarships for x in bestStudents) and all(x in allStudents for x in scholarships) and len(allStudents) != len(scholarships)
