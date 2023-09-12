import os

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from ..persistent.persistent import Persistent


class Visualize:
    def __init__(self, filename='persis.xlsx'):
        """Read or write the workbook specified by filename

        :param filename: the file to manipulate
        :type filename: string
        """
        self.filename = filename

        self.cdir = os.path.dirname(__file__)
        self.font_path = f'{self.cdir}/simsun.ttf'
        self.stopwords_path = f'{self.cdir}/stopwords.txt'

        if not os.path.exists(self.font_path):
            return
        if not os.path.exists(self.stopwords_path):
            return

        self.stopwords = set()
        with open(self.stopwords_path, 'r') as f:
            self.stopwords.update([
                line.strip() for line in
                f.readlines()
            ])
        self.comment_list = []
        self.text = ''

        self.per = Persistent(self.filename)

    def readcomments(self):
        """Get the comment list from the specified filename."""
        self.comment_list = self.per.read()

    def cutword(self):
        """Cut the sentence in the comment list.
        The result is delimited by space.
        """
        for item in self.comment_list:
            self.text += ' '.join(jieba.cut(item))

    def render(self):
        """Visualizing the result."""
        wordcloud = WordCloud(
            font_path=self.font_path,
            width=700,
            height=700,
            background_color='white',
            stopwords=self.stopwords).generate(self.text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def run(self):
        try:
            self.readcomments()
            self.cutword()
            self.render()
        except Exception as e:
            raise e
