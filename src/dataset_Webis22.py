import pandas as pd
import os.path


WEBIS22_PATH = "/dataset/webis-clickbait-22/"
script_dir = os.path.dirname(os.path.abspath(__file__))
TRAIN_FILE = "train.jsonl"
VALIDATION_FILE = "validation.jsonl"


class Webis22:
    """
    self.corpus: (post, text, truthMean)
    """

    """
    path should be dataset/webis-clickbait-22/
    """

    def __init__(self):
        path = script_dir + WEBIS22_PATH
        self.train_file = path + TRAIN_FILE
        self.truth_file = path + VALIDATION_FILE
        df_train = pd.read_json(self.train_file, lines=True)
        df_truth = pd.read_json(self.truth_file, lines=True)
        self.size = df_train.shape[0]

        #truth_id, truth_mean = list(df_truth["uuid"]), list(df_truth["truthMean"])
        #truth_dict = {truth_id[i]: truth_mean[i] for i in range(self.size)}
        train_id, train_post, train_text = (
            list(df_train["uuid"]),
            list(df_train["postText"]),
            list(df_train["targetParagraphs"]),
        )
        # ? train_post[i] is a list
        self.corpus = [
            (
                train_post[i][0],
                " ".join(para for para in train_text[i]),
                #truth_dict[train_id[i]],
            )
            for i in range(self.size)
        ]

        print(self.corpus[:10])


webis22 = Webis22()


"""
Sample data
{
    "uuid": "0af11f6b-c889-4520-9372-66ba25cb7657",
    "postId": "532quh",
    "postText": [
        "Wes Welker Wanted Dinner With Tom Brady, But Patriots QB Had Better Idea"
    ],
    "postPlatform": "reddit",
    "targetParagraphs": [
        "It’ll be just like old times this weekend for Tom Brady and Wes Welker.",
        "Welker revealed Friday morning on a Miami radio station that he contacted Brady because he’ll be in town for Sunday’s game between the New England Patriots and Miami Dolphins at Gillette Stadium. It seemed like a perfect opportunity for the two to catch up.",
        'But Brady’s definition of "catching up" involves far more than just a meal. In fact, it involves some literal "catching" as the Patriots quarterback looks to stay sharp during his four-game Deflategate suspension.',
        '"I hit him up to do dinner Saturday night. He’s like, ‘I’m going to be flying in from Ann Arbor later (after the Michigan-Colorado football game), but how about that morning we go throw?’ " Welker said on WQAM, per The Boston Globe. "And I’m just sitting there, I’m like, ‘I was just thinking about dinner, but yeah, sure. I’ll get over there early and we can throw a little bit.’ "',
        "Welker was one of Brady’s favorite targets for six seasons from 2007 to 2012. It’s understandable him and Brady want to meet with both being in the same area. But Brady typically is all business during football season. Welker probably should have known what he was getting into when reaching out to his buddy.",
        '"That’s the only thing we really have planned," Welker said of his upcoming workout with Brady. "It’s just funny. I’m sitting there trying to have dinner. ‘Hey, get your ass up here and let’s go throw.’ I’m like, ‘Aw jeez, man.’ He’s going to have me running like 2-minute drills in his backyard or something."',
        "Maybe Brady will put a good word in for Welker down in Foxboro if the former Patriots wide receiver impresses him enough.",
    ],
    "targetTitle": "Wes Welker Wanted Dinner With Tom Brady, But Patriots QB Had A Better Idea",
    "targetDescription": "It'll be just like old times this weekend for Tom Brady and Wes Welker. Welker revealed Friday morning on a Miami radio station that he contacted Brady because he'll be in town for Sunday's game between the New England Patriots and Miami Dolphins at Gillette Stadium.",
    "targetKeywords": "new england patriots, ricky doyle, top stories,",
    "targetMedia": [
        "http://pixel.wp.com/b.gif?v=noscript",
        "http://b.scorecardresearch.com/p?c1=2&c2=6783782&cv=2.0&cj=1",
        "http://s.wordpress.com/wp-includes/images/rss.png?m=1354137473h",
        "https://nesncom.files.wordpress.com/2017/03/paul-worrilow.jpg?w=400",
        "http://ssl-nesn-com-255369.c-col.com",
        "http://nesncom.files.wordpress.com/2015/07/yardbarker-fox-sidebar-logo.gif?w=300&h=33",
        "http://pixel.quantserve.com/pixel/p-0eFueme2jAuMI.gif",
        "https://s0.wp.com/wp-content/themes/vip/plugins/lazy-load/images/1x1.trans.gif",
        "https://nesncom.files.wordpress.com/2017/03/brandon-marshall.jpg?w=400",
        "https://nesncom.files.wordpress.com/2017/03/liverpool-vs-arsenal-2017-live-blog-premier-league-week-27.jpg?w=400",
        "https://nesncom.files.wordpress.com/2017/03/usatsi_9913527.jpg?w=400",
        "https://nesncom.files.wordpress.com/2017/03/david-price4.jpg?w=400",
        "https://nesncom.files.wordpress.com/2017/03/usatsi_9914527.jpg?w=400",
        "https://nesncom.files.wordpress.com/2017/03/eric-decker.jpg?w=400",
        "http://nesncom.files.wordpress.com/2015/06/transparent.gif?w=1&h=1",
        "https://nesncom.files.wordpress.com/2015/09/tom-brady-wes-welker.jpg",
        "https://nesncom.files.wordpress.com/2017/03/john-ross1.jpg?w=400",
        "https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=RPMTh1aUXR00Ug",
    ],
    "targetUrl": "http://nesn.com/2016/09/wes-welker-wanted-dinner-with-tom-brady-but-patriots-qb-had-better-idea/",
    "provenance": {
        "source": "anonymized",
        "humanSpoiler": "They Threw A Football",
        "spoilerPublisher": "savedyouaclick",
    },
    "spoiler": ["how about that morning we go throw?"],
    "spoilerPositions": [[[3, 151], [3, 186]]],
    "tags": ["passage"],
}
"""

"""
Below is webis 2017
{
    "id": "608310377143799810",
    "postTimestamp": "Tue Jun 09 16:31:10 +0000 2015",
    "postText": [
        "Apple's iOS 9 'App thinning' feature will give your phone's storage a boost"
    ],
    "postMedia": [],
    "targetTitle": "Apple gives back gigabytes: iOS 9 'app thinning' feature will finally give your phone's storage a boost",
    "targetDescription": "'App thinning' will be supported on Apple's iOS 9 and later models. It ensures apps use the lowest amount of storage space by 'slicing' it to work on individual handsets (illustrated).",
    "targetKeywords": "Apple,gives,gigabytes,iOS,9,app,thinning,feature,finally,phone,s,storage,boost",
    "targetParagraphs": [
        "Paying for a 64GB phone only to discover that this is significantly reduced by system files and bloatware is the bane of many smartphone owner's lives. ",
        "And the issue became so serious earlier this year that some Apple users even sued the company over it. ",
        "But with the launch of iOS 9, Apple is hoping to address storage concerns by introducing a feature known as 'app thinning.'",
        "It has been explained on the watchOS Developer Library site and is aimed at developers looking to optimise their apps to work on iOS and the watchOS. ",
        "It ensures apps use the lowest amount of storage space on a device by only downloading the parts it needs run on the particular handset it is being installed onto.",
        "It 'slices' the app into 'app variants' that only need to access the specific files on that specific handset. ",
        "XperiaBlog recently spotted that the 8GB version of Sony's mid-range M4 Aqua has just 1.26GB of space for users. ",
        "This means that firmware, pre-installed apps and Android software take up a staggering 84.25 per cent. ",
        "Sony does let users increase storage space using a microSD card, but as XperiaBlog explained: 'Sony should never have launched an 8GB version of the Xperia M4 Aqua. ",
        "'If you are thinking about purchasing this model, be aware of what you are buying into.'",
        "Previously, apps would need to be able to run on all handsets and account for the varying files, chipsets and power so contained sections that weren't always relevant to the phone it was being installed on.",
        "This made them larger than they needed to be. ",
        "Under the new plans, when a phone is downloaded from the App Store, the app recognises which phone it is being installed onto and only pulls in the files and code it needs to work on that particular device. ",
        "For iOS, sliced apps are supported on the latest iTunes and on devices running iOS 9.0 and later. ",
        "In all other cases, the App Store will deliver the previous 'universal apps' to customers.",
        "The guidelines also discuss so-called 'on-demand resources.' This allows developers to omit features from an app until they are opened or requested by the user. ",
        "The App Store hosts these resources on Apple servers and manages the downloads for the developer and user. ",
        "This will also increase how quickly an app downloads. ",
        "An example given by Apple is a game app that may divide resources into game levels and request the next level of resources only when the app anticipates the user has completed the previous level.",
        "Similarly, the app can request In-App Purchase resources only when the user buys a corresponding in-app purchase.",
        "Apple explained the operating system will then 'purge on-demand resources when they are no longer needed and disk space is low', removing them until they are needed again.",
        "And the whole iOS 9 software has been designed to be thinner during updates, namely from 4.6GB to 1.3GB, to free up space. ",
        "This app thinning applies to third-party apps created by developers. ",
        "Apple doesn't say if it will apply to the apps Apple pre-installed on devices, such as Stocks, Weather and Safari - but it is likely that it will in order to make iOS 9 smaller. ",
        "As an example of storage space on Apple devices, a 64GB Apple iPhone 6 is typically left with 56GB of free space after pre-installed apps, system files and software is included. ",
        "A drop of 8GB, leaving 87.5 per cent of storage free. ",
        "By comparison, Samsung's 64GB S6 Edge has 53.42GB of available space, and of this 9GB is listed as system memory. ",
        "Although this is a total drop of almost 11GB, it equates to 83 per cent of space free. ",
        "By comparison, on a 32GB S6 MailOnline found 23.86GB of space was available, with 6.62GB attributed to system memory.",
        "This is a drop of just over 8GB and leaves 75 per cent free.",
        "Samsung said it, too, had addressed complaints about bloatware and storage space with its S6 range.  ",
        "Previous handsets, including the Samsung Galaxy S4 and Apple iPhone 5C typically ranged from between 54 per cent and 79 per cent of free space.",
        " ",
        "Businessman 'killed his best friend when he crashed jet-powered dinghy into his £1million yacht while showing off' as his wife filmed them",
    ],
    "targetCaptions": [
        "'App thinning' will be supported on Apple's iOS 9 and later models. It ensures apps use the lowest amount of storage space on a device by only downloading the parts it needs to run on individual handsets. It 'slices' the app into 'app variants' that only need to access the specific files on that specific device",
        "'App thinning' will be supported on Apple's iOS 9 and later models. It ensures apps use the lowest amount of storage space on a device by only downloading the parts it needs to run on individual handsets. It 'slices' the app into 'app variants' that only need to access the specific files on that specific device",
        "The guidelines also discuss so-called 'on-demand resources.' This allows developers to omit features from an app until they are opened or requested by the user. The App Store hosts these resources on Apple servers and manages the downloads for the developer and user. This will also increase how quickly an app downloads",
        "The guidelines also discuss so-called 'on-demand resources.' This allows developers to omit features from an app until they are opened or requested by the user. The App Store hosts these resources on Apple servers and manages the downloads for the developer and user. This will also increase how quickly an app downloads",
        "Apple said it will then 'purge on-demand resources when they are no longer needed and disk space is low' (Apple's storage menu is pictured)",
        "Apple said it will then 'purge on-demand resources when they are no longer needed and disk space is low' (Apple's storage menu is pictured)",
        "A 64GB Apple iPhone 6 is typically left with 56GB of free space after pre-installed apps, system files and software is included. A drop of 8GB, leaving 87.5 % of storage free. Previous handsets, including the Samsung Galaxy S4 and Apple iPhone 5C typically ranged from between 54% and 79% of free space (illustrated)",
        "A 64GB Apple iPhone 6 is typically left with 56GB of free space after pre-installed apps, system files and software is included. A drop of 8GB, leaving 87.5 % of storage free. Previous handsets, including the Samsung Galaxy S4 and Apple iPhone 5C typically ranged from between 54% and 79% of free space (illustrated)",
        "Earlier this year, a pair of disgruntled Apple users filed a lawsuit in Miami accusing the tech giant of 'concealing, omitting and failing to disclose' that on 16GB versions of iPhones, more than 20% of the advertised space isn't available. This graph reveals the capacity available and unavailable to the user",
        "Earlier this year, a pair of disgruntled Apple users filed a lawsuit in Miami accusing the tech giant of 'concealing, omitting and failing to disclose' that on 16GB versions of iPhones, more than 20% of the advertised space isn't available. This graph reveals the capacity available and unavailable to the user",
    ],
}


{
    "id": "608310377143799810",
    "truthJudgments": [0.0, 0.6666667, 0.0, 0.33333334, 0.0],
    "truthMean": 0.2,
    "truthMedian": 0.0,
    "truthMode": 0.0,
    "truthClass": "no-clickbait",
}
"""