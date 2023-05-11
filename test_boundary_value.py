def get_grade(score):
    """
    Function to calculate grade based on score
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def test_boundary_values():
    """
    Function to test boundary values using boundary value analysis
    """
    boundary_test_cases = [(0, "F"), (59, "F"), (60, "D"), (69, "D"), (70, "C"), (79, "C"), (80, "B"), (89, "B"), (90, "A"), (100, "A")]
    for test_case in boundary_test_cases:
        assert get_grade(test_case[0]) == test_case[1], f"Expected {test_case[1]} but got {get_grade(test_case[0])}"

if __name__ == "__main__":
    test_boundary_values()

    print("All tests passed!")

# Kode ini menggunakan teknik Boundary Value Analysis pada sebuah fungsi `get_grade()` yang menghitung nilai grade berdasarkan skor yang diberikan. Fungsi tersebut memiliki beberapa kondisi yang memproses skor dan mengembalikan nilai grade yang sesuai dengan rentang skor.

# Pada kode pengujian, terdapat sebuah fungsi `test_boundary_values()` yang melakukan pengujian pada nilai-nilai batas. Fungsi tersebut melakukan iterasi pada `boundary_test_cases`, yang merupakan sebuah daftar pasangan nilai skor dan nilai grade yang diharapkan. 

# Setiap pasangan nilai skor dan nilai grade diuji dengan memanggil fungsi `get_grade()` dan membandingkan nilai yang dikembalikan dengan nilai grade yang diharapkan. Pengujian dilakukan dengan menggunakan asserstion statement pada baris ke-14, dimana jika fungsi `get_grade()` mengembalikan nilai yang tidak sesuai dengan nilai grade yang diharapkan, maka assertion statement akan gagal dan mengembalikan pesan error yang menjelaskan kesalahan yang terjadi.

# Pada blok `if __name__ == "__main__":`, fungsi pengujian `test_boundary_values()` dipanggil dan program akan mengecek apakah semua pengujian telah berhasil dilakukan atau tidak. Jika semua pengujian berhasil dilakukan, maka program akan mencetak pesan "All tests passed!" untuk menandakan bahwa kode pengujian berjalan dengan baik dan fungsi `get_grade()` telah mengembalikan nilai grade yang diharapkan pada semua kasus uji yang diuji menggunakan teknik Boundary Value Analysis.
