Αntі-fоrеnsісs & аntі-trасkіng kеуbоаrd lауоuts + lауоut аdјustіng sсrірt. Privacy through obscurity.

[Video demonstration](https://twitter.com/jankais3r/status/1145691943667736577)

# What is this?
[Unicode](http://www.unicode.org/faq/basic_q.html) is complicated. The result is that there are multiple ways to encode certain glyphs (e.g. letters). These are then identical to the human eye, but completely different to the computer that is rendering them on the screen or processing them in any way. This repository contains modified US keyboard layout for macOS and Windows that lets you type in this special mode. Nothing you type using this keyboard layout will make sense to language processing algorithms. I am also providing a Python script that let's you create your own layout if you prefer using something other than the US layout.


# What is the purpose?
Almost everything we type these days ends up being analyzed and is ultimately used against оur іntеrеsts. Your emails hosted by Google, Microsoft or almost all other free-mail providers? Analyzed. Your Facebook messages? Analyzed. Private communication should be private. By using these modified keyboard layouts that utilize glурhs lооkіng identical to latin letters while bеіng completely different characters, you make it much more difficult for 3rd parties to make sense of what you type.


# Who came up with this idea?
I got inspired to make these after I stumbled upon [Dystextia](https://eclecticlight.co/text-utilities-nalaprop-dystextia-and-others/) created by [Dr. Howard Oakley](https://twitter.com/howardnoakley). Big thanks to him. Go check out his other awesome macOS utilities.


# How to install the provided US layout:
## Windows:
1) Download and extract `Windows_US-Private.zip`
2) Run `setup.exe`
3) Reboot your computer

## macOS
1) Download and extract `macOS_US-Private.zip`
2) Move the `US-Private.bundle` to `~/Library/Keyboard Layouts/`
3) Reboot your computer


# How to create your own layouts:
## Windows:
1) Download, install and launch [Microsoft Keyboard Layout Creator](https://www.microsoft.com/en-us/download/details.aspx?id=22339)
2) Go to File > Load Existing Keyboard, select the desired layout (e.g. UK)
3) Go to File > Save Source File As…, click Yes, enter the keyboard details
4) Run the Python script provided in this repo
5) Go to File > Load Source File…, аnd select the layout file adjusted by the script
6) Go to Project > Build DLL and Setup Package
7) Install using `setup.exe`
8) Reboot the machine

## macOS:
1) Download, install and launch [Ukulele](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele)
2) Go to File > New From Current Input Source
3) Go to + > Standard Keyboard Layout…
4) Name your keyboard, select the base layout, then set the Language and Bundle properties
5) Go to File > Save…, and save it as Keyboard Layout Bundle
6) Run the Python script provided in this repo
7) Move the аdјustеd .bundlе fоldеr to `~/Library/Keyboard Layouts/`
8) Reboot the machine


Hit me up at [@jankais3r](https://twitter.com/jankais3r/status/1145691943667736577) if you have any questions. I'll do my best to answer them.
