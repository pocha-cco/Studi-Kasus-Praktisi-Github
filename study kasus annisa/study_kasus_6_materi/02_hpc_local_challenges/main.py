from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
import math
import os
import random

def chunk_stats(values):
    # Menghitung jumlah kuadrat untuk ilustrasi beban komputasi.
    return sum(math.sqrt(x * x + 1) for x in values)

def main():
    random.seed(42)
    n = 1_200_000
    values = [random.random() * 100 for _ in range(n)]
    chunks = [values[i:i + n // 4] for i in range(0, n, n // 4)]

    start = perf_counter()
    serial = sum(chunk_stats(chunk) for chunk in chunks)
    serial_time = perf_counter() - start

    start = perf_counter()
    with ProcessPoolExecutor(max_workers=min(4, os.cpu_count() or 1)) as pool:
        parallel = sum(pool.map(chunk_stats, chunks))
    parallel_time = perf_counter() - start

    print("SIMULASI HPC: Analisis data sensor banjir")
    print(f"Jumlah data: {n:,}")
    print(f"Hasil serial : {serial:.4f} | waktu: {serial_time:.3f} detik")
    print(f"Hasil paralel: {parallel:.4f} | waktu: {parallel_time:.3f} detik")
    print(f"Speedup terukur: {serial_time / parallel_time:.2f}x")
    print("\\nCatatan: hasil waktu dipengaruhi CPU, overhead proses, dan ukuran data.")
    print("Dalam kasus nyata, data dapat berasal dari sensor tinggi muka air sungai.")

if __name__ == "__main__":
    main()
