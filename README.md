cs109-dl-videos
===============

Shell script to scrape Harvard CS109 (Intro to Data Science) lecture videos

Overview
---

This is a basic shell script that downloads all the lecture/section videos associated with the CS109 (Intro to Data Science) course run in 2013 by Harvard University.

Usage
---
  
```
./get.sh hq-urls.txt # for high quality versions
```

or...

```
./get.sh lq-urls.txt # for lower quality
```

This will download the videos in the same folder as the shell script as `video*.mp4`.

Requires `rtmpdump`, which can be downloaded [here](https://rtmpdump.mplayerhq.hu/). Or if you're on a Debian-based distro, just install it by running `sudo apt-get install rtmpdump`.

Credit goes to [Ketan](http://www.quora.com/Downloads/How-can-I-download-the-videos-for-CS109-Harvards-Data-Science-Course) over at Quora for the `rtmpdump` command that makes this possible.

Other materials
---

* [Lecture slides](https://drive.google.com/folderview?id=0BxYkKyLxfsNVd0xicUVDS1dIS0k&usp=sharing)
* [Homeworks and labs](https://github.com/cs109/content)
