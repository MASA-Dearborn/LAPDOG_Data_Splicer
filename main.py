import os

def desegment(message_name : str):
    directory = './log/' + message_name
     
    with open(os.path.abspath('./log/' + message_name + '/' + message_name + '.txt'), 'w') as writeFile: #change .txt to .log after debug

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)

            if os.path.isfile(f):
                readFile = open(f,'r')
                writeFile.write(readFile.read() + '\n') 

if __name__ == '__main__':

    for folder in os.listdir('./log/'):
        desegment(folder)

