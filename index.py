from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import wikipedia as wiki
from PyQt5.uic import loadUiType

ui,_=loadUiType('wisdom.ui')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title = 'Wisdom by t0xic0der'
        self.setupUi(self)
        self.handle_buttons()

    def handle_buttons(self):
        self.box_smry.setReadOnly(True)
        self.box_sgst.setReadOnly(True)
        self.box_cont.setReadOnly(True)
        self.btn_find.clicked.connect(self.fetch_data)
        self.btn_relt.clicked.connect(self.fetch_relt)
        self.btn_imgs.clicked.connect(self.fetch_imgs)
        self.btn_rfer.clicked.connect(self.fetch_rfer)
        self.btn_loca.clicked.connect(self.dsply_lang)
        self.btn_docs.clicked.connect(self.fetch_docs)
        self.btn_dnat.clicked.connect(self.fetch_dnat)

    def fetch_rfer(self):
        prdct = self.box_sear.text()
        try:
            self.tex_name.setText("References")
            srch_rslt=wiki.search(prdct)
            paej = wiki.page(srch_rslt[0])
            relt = self.formt_rfer(paej.references)
            self.box_cont.setPlainText(relt)
            self.head_cont.setText("References for '"+str(prdct)+"'")
            self.box_smry.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("A references page has no URL")
        except Exception as e:
            print(e)
            self.tex_name.setText("References")
            self.tex_name.setText("References - Failed to display content")
            self.tex_wiki.setText("  Your keywords were either modified or deleted")
            self.head_cont.setText("Failed to display the list of references")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

    def fetch_relt(self):
        prdct = self.box_sear.text()
        try:
            self.tex_name.setText("Related articles")
            srch_rslt=wiki.search(prdct)
            paej = wiki.page(srch_rslt[0])
            relt = self.formt_relt(paej.links)
            self.box_cont.setPlainText(relt)
            self.head_cont.setText("Related links for '"+str(prdct)+"'")
            self.box_smry.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An related articles page has no URL")
        except Exception as e:
            print(e)
            self.tex_name.setText("Related articles")
            self.tex_name.setText("Related links - Failed to display content")
            self.tex_wiki.setText("  Your keywords were either modified or deleted")
            self.head_cont.setText("Failed to display the list of related links")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

    def fetch_imgs(self):
        prdct = self.box_sear.text()
        try:
            self.tex_name.setText("Image sources")
            srch_rslt=wiki.search(prdct)
            paej = wiki.page(srch_rslt[0])
            imgs = self.formt_imgs(paej.images)
            self.box_cont.setPlainText(imgs)
            self.head_cont.setText("Image sources for '"+str(prdct)+"'")
            self.box_smry.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An image sources page has no URL")
        except Exception as e:
            print(e)
            self.tex_name.setText("Image sources")
            self.tex_name.setText("Image sources - Failed to display content")
            self.tex_wiki.setText("  Your keywords were either modified or deleted")
            self.head_cont.setText("Failed to display the list of image sources")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

    def fetch_dnat(self):
        try:
            self.tex_name.setText("Donate to Wikipedia")
            dnat="Wikipedia is one of the most visited websites in the world.\n\nCommerce is fine. Advertising is not evil. But it doesn't belong here. Not in Wikipedia.\n\nWikipedia is something special. It is like a library or a public park. It is like a temple for the mind. It is a place we can all go to think, to learn, to share our knowledge with others.\n\nWhen I founded Wikipedia, I could have made it into a for-profit company with advertising banners, but I decided to do something different. We’ve worked hard over the years to keep it lean and tight. We fulfill our mission efficiently.\n\nIf everyone reading this donated, our fundraiser would be done within an hour. But not everyone can or will donate. And that's fine. Each year just enough people decide to give.\n\nThis year, please consider making a donation of or whatever you can to protect and sustain Wikipedia.\n\nThanks,\n\nJimmy Wales\nWikipedia Founder "
            self.box_cont.setPlainText(dnat)
            self.box_smry.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.head_cont.setText("From Wikipedia founder Jimmy Wales")
            self.art_url_disp.setText("A donation page has no URL")
            wiki.donate()
        except Exception as e:
            self.tex_name.setText("Donate to Wikipedia")
            self.head_cont.setText("Failed to retrieve the donation link")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

    def dsply_lang(self):
        try:
            self.tex_name.setText("Supported languages")
            content="Wikipedia provides content in the following languages\n"
            list_of_languages=wiki.languages().values()
            for lenguiz in list_of_languages:
                content+=str(str(lenguiz)+"\n")
            self.box_cont.setPlainText(content)
            self.box_smry.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.head_cont.setText("Wisdom currently supports only English language")
            self.art_url_disp.setText("An language page has no URL")
        except Exception as e:
            self.tex_name.setText("Supported languages")
            self.head_cont.setText("Failed to retrieve the list of supported languages")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

    def fetch_docs(self):
        try:
            self.tex_name.setText("Documentation")
            docs="Documentation of the API used here can be found in the links provided below\n\nDocumentation\nhttps://wikipedia.readthedocs.io/en/latest/code.html#api\n\nQuickstart\nhttps://wikipedia.readthedocs.io/en/latest/quickstart.html#quickstart"
            self.box_cont.setPlainText(docs)
            self.box_smry.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.head_cont.setText("API Documentation")
            self.art_url_disp.setText("A documentation page has no URL")
        except Exception as e:
            self.tex_name.setText("Documentation")
            self.head_cont.setText("Failed to retrieve the documentation")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

    def fetch_abut(self):
        pass

    def dsply_back(self):
        pass

    def formt_sgst(self, array):
        sgst_strg="People also search for \n"
        for i in range(len(array)):
            sgst_strg+=str(array[i])
            if i!=(len(array)-1):
                sgst_strg+="\n"
        return sgst_strg

    def formt_relt(self, array):
        list_of_related="These are the links related \n"
        for i in range(len(array)):
            list_of_related+=str(array[i])
            if i!=(len(array)-1):
                list_of_related+="\n"
        return list_of_related

    def formt_rfer(self, array):
        list_of_references="These are the references used \n"
        for i in range(len(array)):
            list_of_references+=str(array[i])
            if i!=(len(array)-1):
                list_of_references+="\n"
        return list_of_references

    def formt_imgs(self, array):
        list_of_images="These are the image sources used \n"
        for i in range(len(array)):
            list_of_images+=str(array[i])
            if i!=(len(array)-1):
                list_of_images+="\n"
        return list_of_images

    def fetch_data(self):
        prdct = self.box_sear.text()
        try:
            srch_rslt=wiki.search(prdct)
            suggest=self.formt_sgst(srch_rslt)                              # Format list of suggestion using function
            summery=wiki.summary(srch_rslt[0])                              # Fetches summary of the given title
            self.box_smry.setPlainText(summery)                             # Sets summary on the box provided
            self.box_sgst.setPlainText(suggest)                             # Sets suggestion on the box provided
            paej=wiki.page(srch_rslt[0])                                    # Fetches the page data for the given title
            self.box_cont.setPlainText(paej.content)                        # Sets content from the fetched page on the box provided
            self.tex_name.setText(srch_rslt[0])                             # Sets title from the fetched page on the box provided
            self.head_cont.setText(srch_rslt[0])                            # Sets title from the fetched page on the box provided
            self.val_paid.setText(str(paej.parent_id))                      # Sets parent ID from the fetched page on the box provided
            self.val_reid.setText(str(paej.revision_id))                    # Sets revision ID from the fetched page on the box provided
            self.art_url_disp.setText("Visit "+paej.url+" for more")        # Sets URL from the fetched page on the box provided
            self.tex_wiki.setText("  From Wikipedia, the free encyclopedia")
        except wiki.PageError as e:
            print(e)
            self.tex_name.setText("Page Not Found - Keywords do not match any article")
            self.tex_wiki.setText("  Try refining your search string to match results")
            self.head_cont.setText("Keywords do not match any article")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")
        except wiki.DisambiguationError as e:
            print(e)
            self.tex_name.setText("Disambiguation - Too many results to choose from")
            self.tex_wiki.setText("  Try refining your search keyword to fetch particular results")
            self.head_cont.setText("There are way too many results!")
            self.box_cont.setPlainText("Seems like your search query was too generalised that it fetched multiple results. Do not fret for it happens with the best of us. Just pick any one from the suggestions provided on the right side to move forward or be a bit more specific about what you are looking for")
            self.box_smry.clear()
            self.box_sgst.clear()
            self.box_sgst.setPlainText(str(e))
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")
        except wiki.HTTPTimeoutError as e:
            print(e)
            self.tex_name.setText("HTTP Timeout - Taking too long to fetch results")
            self.tex_wiki.setText("  Please wait for sometime before trying again")
            self.head_cont.setText("Taking too long to fetch results")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")
        except wiki.WikipediaException as e:
            print(e)
            self.tex_name.setText("Aww snap! - It's not you, It is me")
            self.tex_wiki.setText("  We are experiencing problems at our end")
            self.head_cont.setText("It's not you, It is me")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")
        except:
            self.tex_name.setText("Processing Error - Unable to fetch results")
            self.tex_wiki.setText("  Check the keywords and your internet connection once")
            self.head_cont.setText("Unable to fetch results")
            self.box_smry.clear()
            self.box_cont.clear()
            self.box_sgst.clear()
            self.val_paid.setText("UNDEFINED")
            self.val_reid.setText("UNDEFINED")
            self.art_url_disp.setText("An errored page has no URL")

def main():
    app=QApplication(sys.argv)
    QFontDatabase.addApplicationFont("AkzidenzGroteskLight.ttf")
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()