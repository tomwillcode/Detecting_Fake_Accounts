# Detecting Fake Accounts
Today on most major social media platforms, fake accounts impersonating other people are unfortunately far too common. They may be used for fraud or other malicious purposes. In this github repo you can see a POC for a method that can be implemented through cron-jobs and batch processing. With this method using "unique name identifiers", computer vision, and NLP it is possible to easily detect and remove such impersonating accounts. Below one can see an example of a real account and a fake account on Twitter/X.

# Real Account:
![image](https://github.com/tomwillcode/Detecting_Fake_Accounts/blob/master/Resources/Real_Jeff_Bezos.jpg)

# Fake Account:
![image](https://github.com/tomwillcode/Detecting_Fake_Accounts/blob/master/Resources/Fake_Jeff_Bezos.jpg)

# Regarding Fake Accounts
Above we see an example of the real account for Jeff Bezos and a fake account immitating it almost to a T. It is important to note that sometimes fraud and clearly malicious purposes are not the intention of such accounts. Some of these accounts may simply be created for fun. There are also many fan accounts, meme accounts and so on, that are not intending to impersonate anyone, but essentially serve as a fan-page for a given person. 

# An Automated Method for Detecing Fake Accounts
The method seen in this repo in the notebook Detecting_Fake_Accounts_Main.ipynb, works like this:

1) Map every user to a "unique name identifer" (UNI) so that any unneccessary characters are removed: "Will Edwards" -> 'willedwards', and 'Real Will Edwards' -> 'willedwards', and 'will_edwards' -> 'willedwards'
2) Merge verified accounts with non-verified accounts on the UNI (inner join).
3) Compare bio, usernames etc., with NLI or another form of NLP to detect evidence for fraud, or conversely good natured tributes
4) Compare pictures using Computer Vision in this case using the DeepFace library

Current testing shows that this approach is promising, although it will be better to try and build the most light weight neural network possible that can map any user name to a unique name identifier. I think since there are so many names and so many contingencies anything rules based will ultimately have to be more expensive. 
Further testing should also be used to see what is the most reliable and inexpensive model for the computer vision aspect. With DeepFace you can try different options for detecting and extracting a face from a photo and different models for comparing two faces.



