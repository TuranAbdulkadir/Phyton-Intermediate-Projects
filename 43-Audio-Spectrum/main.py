import wave
import numpy as np
import matplotlib.pyplot as plt

filename = "ses.wav"

try:
    # Ses dosyasını oku
    wav_obj = wave.open(filename, 'rb')
    sample_freq = wav_obj.getframerate()
    n_samples = wav_obj.getnframes()
    signal_wave = wav_obj.readframes(n_samples)
    
    # Sinyali numpy dizisine çevir
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    
    # Zaman ekseni
    times = np.linspace(0, n_samples/sample_freq, num=n_samples)
    
    print("Grafik çiziliyor...")
    plt.figure(figsize=(12, 4))
    plt.plot(times, signal_array, color='purple')
    plt.title(f'Ses Dalga Formu: {filename}')
    plt.ylabel('Sinyal Gücü')
    plt.xlabel('Zaman (saniye)')
    plt.show()

except FileNotFoundError:
    print("❌ 'ses.wav' bulunamadı.")