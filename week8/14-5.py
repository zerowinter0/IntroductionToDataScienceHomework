import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 读取MP3文件
file_path = "c:/Users/Alex/Desktop/数据科学导论作业/week8/moon.mp3"
y, sr = librosa.load(file_path)

# 进行FFT
fft_result = np.fft.fft(y)
magnitude = np.abs(fft_result)
frequency = np.fft.fftfreq(len(fft_result), d=1/sr)

# 可视化
plt.figure(figsize=(12, 6))

# 原始波形
plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title('Original Audio Signal')

# FFT结果
plt.subplot(2, 1, 2)
plt.plot(frequency, magnitude)
plt.title('FFT Result')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
