import matplotlib.pyplot as plt
from PIL import Image

def create_image(sentences):
    '''
    Input - list of sentences(strings)
    Output - Image 
    Creates an image containing handwritten charaacaters from the text sentences.
    '''
    num_sentence = len(sentences)
    max_len = max([len(sentence) for sentence in sentences])

    symbols = ['.']

    fig, axes = plt.subplots(num_sentence, max_len, figsize=(max_len,num_sentence))
    # plt.subplots_adjust(wspace=0, hspace=0)

    for j in range(num_sentence):

        sentence = sentences[j]

        chars = [char for char in sentence]
        chars.extend([' ' for i in range(max_len - len(sentence))])

        for i in range(len(chars)):

            if(chars[i]>='Z'):
                axes[j,i].imshow(Image.open('data/' + chars[i] + '_small.png'))

            elif(chars[i]==' '):
                axes[j,i].imshow(Image.open('data/space.png'))

            elif(chars[i] in symbols):
                axes[j,i].imshow(Image.open('data/space.png'))

            elif(chars[i] == '?'):
                axes[j,i].imshow(Image.open('data/question.jpg'))

            else:
                axes[j,i].imshow(Image.open('data/' + chars[i] + '.png'))

            axes[j,i].axis('off')

    fig.tight_layout(w_pad=-1,h_pad=1)

    return fig