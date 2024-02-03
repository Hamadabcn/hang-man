'''
Hangman Game
-------------------------------------------------------------
'''
import random
import time
import os

def play_again():
  question = 'Do You want to play again? y = yes, n = no \n'
  play_game = input(question)
  while play_game.lower() not in ['y', 'n']:
      play_game = input(question)

  if play_game.lower() == 'y':
      return True
  else:
      return False

def hangman(word):
  display = '_' * len(word)
  count = 0
  limit = 5
  letters = list(word)
  guessed = []
  while count < limit:
      guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
      while len(guess) == 0 or len(guess) > 1:
          print('Invalid input. Enter a single letter\n')
          guess = input(
              f'Hangman Word: {display} Enter your guess: \n').strip()

      if guess in guessed:
          print('Oops! You already tried that guess, try again!\n')
          continue

      if guess in letters:
          letters.remove(guess)
          index = word.find(guess)
          display = display[:index] + guess + display[index + 1:]

      else:
          guessed.append(guess)
          count += 1
          if count == 1:
              time.sleep(1)
              print('   _____ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 2:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 3:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 4:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 5:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '__|__\n')
              print('Wrong guess. You\'ve been hanged!!!\n')
              print(f'The word was: {word}')

      if display == word:
          print(f'Congrats! You have guessed the word \'{word}\' correctly!')
          break


def play_hangman():
   print('\nWelcome to Hangman\n')
   name = input('Enter your name: ')
   print(f'Hello {name}! Best of Luck!')
   time.sleep(3)
   print('The game is about to start!\nLet\'s play Hangman!')
   time.sleep(3)
   os.system('cls' if os.name == 'nt' else 'clear')

   words_to_guess = [
       'image', 'film', 'promise', 'kids','lungs', 'rhyme','plants', 'world','march', ''
       'april', 'may', 'june', 'july','man', 'girl', 'women', 'army', 'almost', 'wonder', 'life', 
       'true', 'python', 'english', 'parking', 'anything', 'watch', 'white', 'black', 'blue'
       'red', 'subway', 'length', 'paris', 'cairo', 'milan', 'madrid', 'istambul','play', 
       'practice', 'run', 'left', 'right', 'empty', 'keyboard', 'computer', 'code', 'coding',
       'cairo', 'orange', 'pink', 'house', 'very', 'sky', 'lawyer', 'pixel', 'wave', 'croquetas', 
       'salmon', 'atun', 'build', 'portugal', 'fun', 'family', 'alone', 'beauty', 'bus', 'queso',
       'tomate', 'pera', 'mobile', 'movil', 'phone', 'web', 'carton', 'car', 'boat', 'balcony', 
       'sofa', 'chair', 'melon', 'water', 'kitchen', 'scramble', 'sound', 'soundtrack', 'track',
       'music', 'frida', 'port', 'airport', 'like', 'love', 'home', 'dream', 'hotel', 'fish',
       'spain', 'spanish', 'french', 'grace', 'dust', 'dustbin', 'bin', 'cup', 'cupboard', 'board',
       'español', 'españa', 'flat', 'port', 'airport', 'plan', 'airplan', 'road', 'lighter', 
       'light', 'torch', 'double', 'question', 'mark', 'marks', 'bar', 'word', 'random', 'while',
       'play', 'choice', 'shock', 'aftershock', 'algorithms', 'abduction', 'abductions', 'back',
       'background', 'authorized', 'autorize', 'bank', 'bankruptcy', 'bankrupted', 'birthday',
       'birthplace', 'place', 'birth', 'blue', 'prints', 'blueprints', 'boyfriend', 'friend', 'boy',
       'break', 'breakdown', 'down', 'clip', 'clipboards', 'compatible', 'tray', 'ashtray', 'ash',
       'complained', 'complain', 'completing', 'corn', 'flakes', 'cornflakes', 'decorating', 'decor',
       'defaulting', 'default', 'destroy', 'destroying', 'education', 'exhausting', 'flamingos',
       'flourished', 'godfathers', 'harvesting', 'hypnotized', 'importance', 'introduces', 'journalism',
       'journal', 'lifeguards', 'gaurds', 'microwaves', 'normalized', 'normal', 'lubricated', 'lubricate',
       'methodical', 'method', 'pork', 'cow', 'lion', 'cat', 'dog', 'tiger', 'monkey', 'key', 'jar',
       'stand', 'sit', 'eat', 'walk', 'take', 'talk', 'when', 'what', 'how', 'who', 'when', 'legal',
       'court', 'courtyard', 'console', 'bug', 'terminal', 'problem', 'problems', 'exit', 'open',
       'close', 'out', 'way', 'wayout', 'heat', 'cold', 'warm', ' rain', 'fog', 'frog', 'park',
       'listen', 'past', 'highlight', 'high', 'heads', 'tails', 'black', 'count', 'countdown',
       'date', 'time', 'dice', 'dominos', 'invert', 'keyword', 'largest', 'mario', 'numbers', 
       'power', 'prime', 'quiz', 'red', 'remove', 'stack', 'rows', 'run', 'snake', 'square',
       'save', 'store', 'sum', 'table', 'underline', 'under', 'line', 'vowels', 'wonder', 'radio',
       'speak', 'any', 'mouse', 'market', 'turkey', 'iraq', 'egypt', 'sudan', 'libya', 'jordan',
       'nike', 'human', 'saudi', 'dubai', 'portsaid', 'ocean', 'india', 'rice', 'iran', 'syria',
       'stars','stairs', 'case', 'staircase', 'carpet', 'cousin', 'grand', 'father', 'mother', 
       'team', 'amount', 'true', 'false', 'understand', 'angle', 'astro', 'astronomer', 'bone',
       'bonefire', 'fire', 'bumpy', 'candle', 'stick', 'candlestick', 'cash', 'visa', 'certain',
       'climb', 'core', 'cover', 'donate', 'farm', 'farming', 'goal', 'goat', 'handy', 'something',
       'islam', 'judo', 'box', 'boxing', 'hair', 'her', 'his', 'go', 'stupid', 'up', 'update', 
       'laugh', 'laughter', 'lizard', 'launch', 'brakefast', 'lunch', 'miner', 'mineral', 'modern',
       'old', 'boring', 'ugly', 'sad', 'nighbour', 'nylon', 'plastic', 'petrol', 'gas', 'gasoline',
       'clock', 'out', 'outline', 'poverty', 'pet', 'pile', 'pyramid', 'quote', 'rash', 'reckon',
       'rent', 'respond', 'skate', 'snow', 'ski', 'alpine', 'winter', 'spring', 'remove',
       'stain', 'shaving', 'show', 'cream', 'simple', 'simply', 'slam', 'slim', 'fat', 'social',
       'sociable', 'sort', 'speck', 'spot', 'sport', 'star', 'sporty', 'stare', 'stock', 'stocking',
       'string', 'sue', 'target', 'tend', 'tent', 'north', 'south', 'east', 'west', 'triumph', 
       'through', 'after', 'before', 'until', 'last', 'up', 'easy', 'uneasy', 'utensil', 'rule',
       'unruley', 'reliable', 'unreliable', 'vertical', 'horizontal', 'volt', 'volume', 'watch',
       'wife', 'husband', 'daughter', 'son', 'mother', 'father', 'brother', 'grandfather', 'paid', 
       'width', 'out', 'turquoise', "in", "out", "father", "come", 
       
       
       
       
       
   ]
   play = True
   while play:
       word = random.choice(words_to_guess)
       hangman(word)
       play = play_again()

   print('Thanks For Playing! come back soon!')
   exit()


if __name__ == '__main__':
  play_hangman()
