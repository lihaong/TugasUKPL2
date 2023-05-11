# Penjelasan

### Penjelasan Teknik Boundary Value Analysis
Kode yang diberikan adalah contoh pengujian menggunakan teknik Boundary Value Analysis pada sebuah fungsi `get_grade()` yang menghitung nilai grade berdasarkan skor yang diberikan. 
Fungsi tersebut memiliki beberapa kondisi yang memproses skor dan mengembalikan nilai grade yang sesuai dengan rentang skor.
Pada kode pengujian, terdapat sebuah fungsi `test_boundary_values()` yang melakukan pengujian pada nilai-nilai batas. 
Fungsi tersebut melakukan iterasi pada `boundary_test_cases`, yang merupakan sebuah daftar pasangan nilai skor dan nilai grade yang diharapkan. 
Setiap pasangan nilai skor dan nilai grade diuji dengan memanggil fungsi `get_grade()` dan membandingkan nilai yang dikembalikan dengan nilai grade yang diharapkan. 
Pengujian dilakukan dengan menggunakan asserstion statement pada baris ke-14, dimana jika fungsi `get_grade()` mengembalikan nilai yang tidak sesuai dengan nilai grade yang diharapkan, maka assertion statement akan gagal dan mengembalikan pesan error yang menjelaskan kesalahan yang terjadi.
Pada blok `if __name__ == "__main__":`, fungsi pengujian `test_boundary_values()` dipanggil dan program akan mengecek apakah semua pengujian telah berhasil dilakukan atau tidak. 
Jika semua pengujian berhasil dilakukan, maka program akan mencetak pesan "All tests passed!" untuk menandakan bahwa kode pengujian berjalan dengan baik dan fungsi `get_grade()` telah mengembalikan nilai grade yang diharapkan pada semua kasus uji yang diuji menggunakan teknik Boundary Value Analysis.

### Penjelasan Teknik Boundary Value Analysis
Teknik kedua adalah teknik State Transition Testing pada sebuah kelas `TrafficLight` yang merepresentasikan sebuah lampu lalu lintas. 
Kelas tersebut memiliki sebuah atribut `state` yang merepresentasikan kondisi saat ini dari lampu lalu lintas, dan sebuah fungsi `change_state()` yang mengubah kondisi dari lampu lalu lintas sesuai dengan aturan transisi yang telah ditentukan.
Pada kode pengujian, terdapat sebuah fungsi `test_state_transition()` yang melakukan pengujian pada semua kemungkinan transisi keadaan pada objek `TrafficLight`. 
Fungsi tersebut melakukan inisialisasi objek `TrafficLight`, dan kemudian memanggil fungsi `change_state()` pada setiap transisi yang mungkin dari setiap kondisi lampu lalu lintas.
Setiap transisi keadaan diuji dengan memanggil fungsi `change_state()` dan membandingkan kondisi yang dikembalikan dengan kondisi yang diharapkan menggunakan assertion statement pada baris ke-11, 14, 17, dan seterusnya. 
Jika kondisi yang dikembalikan tidak sama dengan kondisi yang diharapkan, assertion statement akan gagal dan mengembalikan pesan error yang menjelaskan kesalahan yang terjadi.
Pada blok `if __name__ == "__main__":`, fungsi pengujian `test_state_transition()` dipanggil dan program akan mengecek apakah semua pengujian telah berhasil dilakukan atau tidak. Jika semua pengujian berhasil dilakukan, maka program akan mencetak pesan "All tests passed!" untuk menandakan bahwa kode pengujian berjalan dengan baik dan objek `TrafficLight` telah melakukan transisi antar keadaan secara benar menggunakan teknik State Transition Testing.
