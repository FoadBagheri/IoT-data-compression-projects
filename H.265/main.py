from moviepy.editor import VideoFileClip
import imageio_ffmpeg as ffmpeg
import os


def compress_video(input_path, output_path, codec='libx265', crf=23):
    try:
        clip = VideoFileClip(input_path)

        clip.write_videofile(output_path, codec=codec, fps=10, preset='ultrafast', bitrate=f"{crf}k")

        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        print(f"Original Video Size: {original_size} bytes")
        print(f"Compressed Video Size: {compressed_size} bytes. Check '{output_path}'.")

    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    input_video_path = "input_video.mp4"
    compressed_video_path = "compressed_video.mp4"

    crf_value = 200

    compress_video(input_video_path, compressed_video_path, crf=crf_value)

