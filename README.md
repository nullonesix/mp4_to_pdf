# mp4_to_pdf
Python code to convert an mp4 of a video lecture to a pdf slide deck.

Usage:
```
In a terminal:
git clone https://github.com/nullonesix/mp4_to_pdf
cd mp4_to_pdf
cp [location_of_your_mp4_video_lecture] lecture.mp4
python3 slides.py # to make pngs from video
python3 slides2pdf.py # to make a pdf from pngs
python3 trim_lecture.py # to remove question section at the end
```

- you can adjust similarity threshold in slides.py (default is 0.99, lower threshold means potentially fewer slides are included, higher threshold means potential duplicate slides)
- for faster processing you can increase the frame_rate in slides.py (default is 30, this means any slide that has less than 0.5 seconds spent on it might be excluded)
- for a smaller pdf you can adjust the width in slides.py or switch from png to jpg
