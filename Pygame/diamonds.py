# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set up the game window
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Diamonds Card Game")

# # Define card values and suits
# CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 2 - Ace
# CARD_SUITS = ["Hearts", "Clubs", "Spades", "Diamonds"]
# CARD_COLORS = [(255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255)]  # Red, Black, Black, Blue

# # Define card dimensions
# CARD_WIDTH = 80
# CARD_HEIGHT = 120

# # Define game state variables
# player_hands = [[] for _ in range(4)]
# diamond_deck = []
# auction_pot = []
# player_scores = [0, 0, 0, 0]
# current_player = 0
# game_over = False
# game_message = ""

# # Define font
# FONT_NAME = "arial-cufonfonts\ARIAL.TTF"
# FONT_SIZE = 24
# font = pygame.font.Font(FONT_NAME, FONT_SIZE)

# # Function to deal the cards
# def deal_cards():
#     global player_hands, diamond_deck
    
#     # Deal the non-diamond cards to players
#     for i in range(4):
#         for suit in CARD_SUITS:
#             if suit != "Diamonds":
#                 player_hands[i].append((random.choice(CARD_VALUES), suit))
    
#     # Create the diamond deck
#     for value in CARD_VALUES:
#         diamond_deck.append((value, "Diamonds"))
#     random.shuffle(diamond_deck)

# # Function to display a card
# def draw_card(card, x, y, color):
#     card_value, card_suit = card
    
#     # Draw the card background
#     pygame.draw.rect(screen, (255, 255, 255), (x, y, CARD_WIDTH, CARD_HEIGHT))
#     pygame.draw.rect(screen, color, (x, y, CARD_WIDTH, CARD_HEIGHT), 2)
    
#     # Draw the card value
#     value_text = str(card_value)
#     value_width, value_height = font.size(value_text)
#     value_x = x + CARD_WIDTH // 2 - value_width // 2
#     value_y = y + CARD_HEIGHT // 2 - value_height // 2
#     screen.blit(font.render(value_text, True, color), (value_x, value_y))

# # Function to draw the UI elements
# def draw_ui():
#     # Draw the player's cards
#     for i in range(4):
#         for j, card in enumerate(player_hands[i]):
#             draw_card(card, 50 + j * CARD_WIDTH, 50 + i * CARD_HEIGHT, CARD_COLORS[i])
    
#     # Draw the diamond deck and auction pot
#     for i, card in enumerate(diamond_deck):
#         draw_card(card, 50 + i * CARD_WIDTH, 450, CARD_COLORS[3])
#     for i, card in enumerate(auction_pot):
#         draw_card(card, 50 + i * CARD_WIDTH, 550, CARD_COLORS[3])
    
#     # Draw the player score bars
#     for i in range(4):
#         score_bar_x = 50 + i * (WINDOW_WIDTH // 4)
#         score_bar_y = 700
#         score_bar_width = WINDOW_WIDTH // 4 - 50
#         score_bar_height = 50
#         pygame.draw.rect(screen, CARD_COLORS[i], (score_bar_x, score_bar_y, score_bar_width, score_bar_height))
#         score_text = str(player_scores[i])
#         score_width, score_height = font.size(score_text)
#         score_x = score_bar_x + score_bar_width // 2 - score_width // 2
#         score_y = score_bar_y + score_bar_height // 2 - score_height // 2
#         screen.blit(font.render(score_text, True, (255, 255, 255)), (score_x, score_y))
    
#     # Draw the game message
#     message_text = font.render(game_message, True, (0, 0, 0))
#     message_rect = message_text.get_rect(midtop=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
#     screen.blit(message_text, message_rect)

# # Function to handle user input
# def handle_user_input(mouse_pos):
#     global current_player, auction_pot, game_message
    
#     # Check if the user clicked on a card in their hand
#     for i, card in enumerate(player_hands[current_player]):
#         card_rect = pygame.Rect(50 + i * CARD_WIDTH, 50 + current_player * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
#         if card_rect.collidepoint(mouse_pos):
#             # User clicked on a card, add it to the auction pot
#             auction_pot.append(player_hands[current_player].pop(i))
#             game_message = f"Player {current_player+1} played a card."
#             current_player = (current_player + 1) % 4
#             return

#     # Check if the user clicked on a card in the diamond deck
#     for i, card in enumerate(diamond_deck):
#         card_rect = pygame.Rect(50 + i * CARD_WIDTH, 450, CARD_WIDTH, CARD_HEIGHT)
#         if card_rect.collidepoint(mouse_pos):
#             # User clicked on a diamond card, handle the bidding
#             handle_bidding(i)
#             game_message = f"Diamond card auction in progress."
#             return

# # Function to handle the bidding process
# def handle_bidding(diamond_index):
#     global current_player, auction_pot, player_scores, game_message

#     # Perform the bidding process
#     bids = []
#     for i in range(4):
#         if player_hands[i]:
#             bid_card = player_hands[i].pop(0)
#             bids.append((i, bid_card))

#     if bids:
#         # Determine the winner of the diamond card
#         bids.sort(key=lambda x: CARD_VALUES[x[1][0] - 2], reverse=True)
#         winner, winning_bid = bids[0]
#         player_scores[winner] += winning_bid[0]
#         auction_pot.append(diamond_deck.pop(diamond_index))
#         game_message = f"Player {winner+1} won the {CARD_VALUES[winning_bid[0]-2]} of Diamonds."
#     else:
#         # If there are no bids, discard the diamond card
#         game_message = "No bids for the diamond card. Discarding the card."
#         auction_pot.append(diamond_deck.pop(diamond_index))

#     # Move to the next player's turn
#     current_player = (winner + 1) % 4 if bids else current_player

# # Main game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             handle_user_input(mouse_pos)

#     # Clear the screen
#     screen.fill((255, 255, 255))

#     # Deal the cards if the game is just starting
#     if not player_hands[0] and not diamond_deck:
#         deal_cards()
#         game_message = "Game started. Pick a card from your hand."

#     # Draw the UI elements
#     draw_ui()

#     # Update the display
#     pygame.display.flip()

#     # Check if the game is over
#     if not diamond_deck:
#         game_over = True
#         game_message = "Game Over! Final Scores:"
#         break

# # Game over logic
# if game_over:
#     print(game_message)
#     for i in range(4):
#         print(f"Player {i+1}: {player_scores[i]}")
#     if max(player_scores) == player_scores[0]:
#         print("Player 1 wins!")
#     elif max(player_scores) == player_scores[1]:
#         print("Player 2 wins!")
#     elif max(player_scores) == player_scores[2]:
#         print("Player 3 wins!")
#     else:
#         print("Player 4 wins!")


# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set up the game window
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Diamonds Card Game")

# # Define card values and suits
# CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 2 - Ace
# CARD_SUITS = ["Hearts", "Clubs", "Spades", "Diamonds"]
# CARD_COLORS = [(255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255)]  # Red, Black, Black, Blue

# # Define card dimensions
# CARD_WIDTH = 80
# CARD_HEIGHT = 120

# # Define game state variables
# player_hands = [[] for _ in range(4)]
# diamond_deck = []
# auction_pot = []
# player_scores = [0, 0, 0, 0]
# current_player = 0
# game_over = False
# game_message = "Game starting. Good luck!"

# # Define font
# FONT_NAME = "arial-cufonfonts\ARIAL.TTF"
# FONT_SIZE = 24
# font = pygame.font.Font(FONT_NAME, FONT_SIZE)

# # Function to deal the cards
# def deal_cards():
#     global player_hands, diamond_deck
    
#     # Deal the non-diamond cards to players
#     for i in range(4):
#         for suit in CARD_SUITS:
#             if suit != "Diamonds":
#                 player_hands[i].append((random.choice(CARD_VALUES), suit))
    
#     # Create the diamond deck
#     for value in CARD_VALUES:
#         diamond_deck.append((value, "Diamonds"))
#     random.shuffle(diamond_deck)

# # Function to display a card
# def draw_card(card, x, y, color):
#     card_value, card_suit = card
    
#     # Draw the card background
#     pygame.draw.rect(screen, (255, 255, 255), (x, y, CARD_WIDTH, CARD_HEIGHT))
#     pygame.draw.rect(screen, color, (x, y, CARD_WIDTH, CARD_HEIGHT), 2)
    
#     # Draw the card value
#     value_text = str(card_value)
#     value_width, value_height = font.size(value_text)
#     value_x = x + CARD_WIDTH // 2 - value_width // 2
#     value_y = y + CARD_HEIGHT // 2 - value_height // 2
#     screen.blit(font.render(value_text, True, color), (value_x, value_y))

# # Function to draw the UI elements
# def draw_ui():
#     # Draw the player's cards
#     for i in range(4):
#         for j, card in enumerate(player_hands[i]):
#             draw_card(card, 50 + j * CARD_WIDTH, 50 + i * CARD_HEIGHT, CARD_COLORS[i])
    
#     # Draw the diamond deck and auction pot
#     for i, card in enumerate(diamond_deck):
#         draw_card(card, 50 + i * CARD_WIDTH, 450, CARD_COLORS[3])
#     for i, card in enumerate(auction_pot):
#         draw_card(card, 50 + i * CARD_WIDTH, 550, CARD_COLORS[3])
    
#     # Draw the player score bars
#     for i in range(4):
#         score_bar_x = 50 + i * (WINDOW_WIDTH // 4)
#         score_bar_y = 700
#         score_bar_width = WINDOW_WIDTH // 4 - 50
#         score_bar_height = 50
#         pygame.draw.rect(screen, CARD_COLORS[i], (score_bar_x, score_bar_y, score_bar_width, score_bar_height))
#         score_text = str(player_scores[i])
#         score_width, score_height = font.size(score_text)
#         score_x = score_bar_x + score_bar_width // 2 - score_width // 2
#         score_y = score_bar_y + score_bar_height // 2 - score_height // 2
#         screen.blit(font.render(score_text, True, (255, 255, 255)), (score_x, score_y))
#     # Draw the game message
#     message_text = font.render(game_message, True, (0, 0, 0))
#     message_rect = message_text.get_rect(midtop=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
#     screen.blit(message_text, message_rect)

# # Function to handle user input
# def handle_user_input(mouse_pos):
#     global current_player, auction_pot, game_message
    
#     # Check if the user clicked on a card in their hand
#     for i, card in enumerate(player_hands[current_player]):
#         card_rect = pygame.Rect(50 + i * CARD_WIDTH, 50 + current_player * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
#         if card_rect.collidepoint(mouse_pos):
#             # User clicked on a card, add it to the auction pot
#             auction_pot.append(player_hands[current_player].pop(i))
#             game_message = f"Player {current_player+1} played a card."
#             current_player = (current_player + 1) % 4
#             return

#     # Check if the user clicked on a card in the diamond deck
#     for i, card in enumerate(diamond_deck):
#         card_rect = pygame.Rect(50 + i * CARD_WIDTH, 450, CARD_WIDTH, CARD_HEIGHT)
#         if card_rect.collidepoint(mouse_pos):
#             # User clicked on a diamond card, handle the bidding
#             handle_bidding(i)
#             game_message = f"Diamond card auction in progress."
#             return

# # Function to handle the bidding process
# def handle_bidding(diamond_index):
#     global current_player, auction_pot, player_scores, game_message
    
#     # Perform the bidding process
#     bids = []
#     for i in range(4):
#         if player_hands[i]:
#             bid_card = player_hands[i].pop(0)
#             bids.append((i, bid_card))
    
#     # Determine the winner of the diamond card
#     bids.sort(key=lambda x: CARD_VALUES[x[1][0] - 2], reverse=True)
#     winner, winning_bid = bids[0]
#     player_scores[winner] += winning_bid[0]
#     auction_pot.append(diamond_deck.pop(diamond_index))
#     game_message = f"Player {winner+1} won the diamond card with a {winning_bid[0]}."
    
#     # Move to the next player's turn
#     current_player = (winner + 1) % 4
# # Main game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             handle_user_input(mouse_pos)

#     # Clear the screen
#     screen.fill((255, 255, 255))

#     # Deal the cards if the game is just starting
#     if not player_hands[0] and not diamond_deck:
#         deal_cards()
#         game_message = "Game started. Pick a card from your hand."

#     # Draw the UI elements
#     draw_ui()

#     # Update the display
#     pygame.display.flip()

#     # Check if the game is over
#     if not diamond_deck and all(len(hand) == 0 for hand in player_hands):
#         game_over = True
#         game_message = "Game Over! Final Scores:"
#         break

# # Game over logic
# if game_over:
#     print(game_message)
#     for i in range(4):
#         print(f"Player {i+1}: {player_scores[i]}")
#     if max(player_scores) == player_scores[0]:
#         print("Player 1 wins!")
#     elif max(player_scores) == player_scores[1]:
#         print("Player 2 wins!")
#     elif max(player_scores) == player_scores[2]:
#         print("Player 3 wins!")
#     else:
#         print("Player 4 wins!")

# # Quit Pygame
# pygame.quit()



import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
CARD_WIDTH = 60
CARD_HEIGHT = 70
CARD_SPACING = 20
FONT_SIZE = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Dictionary to store the points for each card
card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
user_cards = ['2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'J', 'Q', 'K', 'A']
# Function to draw a random diamond card


def draw_card(drawn_cards:list[str])-> str:
    diamonds = ['2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'J', 'Q', 'K', 'A']
    available_cards = [card for card in diamonds if card not in drawn_cards]
    if available_cards:
        card = random.choice(available_cards)
        drawn_cards.append(card)
        return card
    else:
        return None


def make_bot_bid(bot_bids, drawn_card):
    # Adjust bot's bid based on drawn card value
    if drawn_card in ['2', '3', '4', '5']:
        bot_bid = random.choice(['2', '3', '4', '5'])
    elif drawn_card in ['6', '7', '8', '9']:
        bot_bid = random.choice(['6', '7', '8', '9'])
    else:  # drawn_card in ['10', 'J', 'Q', 'K', 'A']
        bot_bid = random.choice(['10', 'J', 'Q', 'K', 'A'])

    if bot_bid in bot_bids:
        # Rebid if the chosen bid has been used before
        return make_bot_bid(bot_bids, drawn_card)
    else:
        bot_bids.append(bot_bid)
        return bot_bid

# Function to determine the winner of the round


def determine_winner(user_bid, bot_bid, prize_card):
    if card_points[user_bid] > card_points[bot_bid]:
        return "user"
    elif card_points[user_bid] < card_points[bot_bid]:
        return "bot"
    else:
        return "tie"

# Function to display text


def display_text(screen, text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to display cards


def display_cards(screen, cards, font, user_bids):
    x = (WINDOW_WIDTH - (CARD_WIDTH + CARD_SPACING) * len(cards)) // 2
    y = WINDOW_HEIGHT - CARD_HEIGHT - CARD_SPACING
    for card in cards:
        color = BLACK
        if card in user_bids:
            color = (255, 0, 0)
        pygame.draw.rect(screen, GRAY, (x, y, CARD_WIDTH, CARD_HEIGHT))
        display_text(screen, card, x + CARD_WIDTH // 2,
                     y + CARD_HEIGHT // 2, font, color)
        x += CARD_WIDTH + CARD_SPACING


def display_diamond_card(screen, card, font):
    x = (WINDOW_WIDTH) // 2
    y = WINDOW_HEIGHT // 2
    pygame.draw.rect(screen, GRAY, (x, y, CARD_WIDTH, CARD_HEIGHT))
    display_text(screen, card, x + CARD_WIDTH // 2,
                 y + CARD_HEIGHT // 2, font, BLACK)
# Main function

# Main function


def main():
    # Initialize Pygame window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Diamonds Game")

    # Font for displaying text
    font = pygame.font.Font(None, FONT_SIZE)

    # Initialize game variables
    user_points = 0
    bot_points = 0
    current_round = 1
    rounds = 13  # Total number of rounds
    user_bids = []
    bot_bids = []
    drawn_cards = []

    bot_cards = ['2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K', 'A']
    drawn_card = None
    # Main loop
    running = True
    while running:
        screen.fill(WHITE)
        # Draw a card at the start of the game to set the initial drawn_card value
        if current_round == 1 and not drawn_card:
            drawn_card = draw_card(drawn_cards)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or current_round > rounds:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if user clicked on a card button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                start_x = (WINDOW_WIDTH - (CARD_WIDTH + CARD_SPACING)
                           * len(user_cards)) // 2
                for i, card in enumerate(user_cards):
                    card_rect = pygame.Rect(start_x + i * (CARD_WIDTH + CARD_SPACING),
                                            WINDOW_HEIGHT - CARD_HEIGHT - CARD_SPACING, CARD_WIDTH, CARD_HEIGHT)
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        if card not in user_bids:
                            user_bids.append(card)
                        else:
                            continue
                        if drawn_card:
                            bot_bids.append(
                                make_bot_bid(bot_bids, drawn_card))
                        # Determine the winner of the round
                        winner = determine_winner(
                            user_bids[-1], bot_bids[-1], drawn_card)
                        if winner == "user":
                            user_points += card_points[drawn_card]
                        elif winner == "bot":
                            bot_points += card_points[drawn_card]
                        current_round += 1
                        drawn_card = draw_card(drawn_cards)

                        # Wait for a moment before proceeding to the next round
                        if current_round <= rounds:
                            for i in range(4, 0, -1):
                                screen.fill(WHITE)
                                display_text(
                                    screen, f"Round: {current_round}/{rounds}", 20, 20, font, BLACK)
                                display_text(
                                    screen, f"Your Bid: {user_bids[-1]}", 40, WINDOW_HEIGHT - 120, font, BLACK)
                                display_text(
                                    screen, f"Bot's Bid: {bot_bids[-1]}", WINDOW_WIDTH - 180, WINDOW_HEIGHT - 120, font, BLACK)
                                display_text(
                                    screen, f"Winner: {winner}", WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2, font, BLACK)
                                display_text(
                                    screen, f"Your Score: {user_points}", 40, WINDOW_HEIGHT - 160, font, BLACK)
                                display_text(screen, f"Bot's Score: {bot_points}",
                                             WINDOW_WIDTH - 180, WINDOW_HEIGHT - 160, font, BLACK)
                                display_text(
                                    screen, f"Next Round Starting in {i}...", WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 100, font, BLACK)
                                pygame.display.flip()
                                pygame.time.wait(1000)

                        # Reset the screen for the next round
                        screen.fill(WHITE)
        # Display current round
        # screen.fill(WHITE)
        display_text(
            screen, f"Round: {current_round}/{rounds}", 20, 20, font, BLACK)

        # Display user's cards
        display_cards(screen, user_cards, font, user_bids)
        display_diamond_card(screen, drawn_card, font)
        # Display scores
        display_text(
            screen, f"Your Score: {user_points}", 40, WINDOW_HEIGHT - 160, font, BLACK)
        display_text(screen, f"Bot's Score: {bot_points}",
                     WINDOW_WIDTH - 180, WINDOW_HEIGHT - 160, font, BLACK)

        # Update the display
        pygame.display.flip()

    pygame.quit()


# Run the main function
if __name__ == "__main__":
    main()



# import pygame
# import random
# import os

# pygame.init()
# # Initialize Pygame
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Set the screen dimensions
# SCREEN_WIDTH = 1050
# SCREEN_HEIGHT = 700

# # Set desired card dimensions (adjusted for smaller size)
# CARD_WIDTH = 80
# CARD_HEIGHT = 112  # Adjusted proportionally based on CARD_WIDTH

# # Set font
# FONT = pygame.font.Font(None, 36)
# # Dictionary mapping cards to their values
# CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12, '13': 13, '1': 14}

# # Function to generate a unique random diamond card
# def generate_diamond_card(remaining_cards, used_diamonds):
#     while True:
#         card = random.choice(remaining_cards)
#         if card not in used_diamonds:
#             used_diamonds.append(card)
#             return card

# def generate_computer_bid(computer_deck, revealed_diamonds):
#     # Sort computer's deck based on card values
#     sorted_computer_deck = sorted(computer_deck, key=lambda card: CARD_VALUES[card])

#     # Find the optimal card to bid based on revealed diamond cards
#     for card in sorted_computer_deck:
#         if card not in revealed_diamonds:
#             return card
    
#     # If no optimal card found (unlikely due to revealed diamonds tracking)
#     return sorted_computer_deck[0]  # Choose the lowest card as fallback

# def load_card_images_suit(card_dir, suit):
#     card_images = {}
#     suit_dir = os.path.join(card_dir, suit)
#     full_path = os.path.join(os.path.dirname(__file__), suit_dir)
#     for card_file in os.listdir(full_path):
#         if card_file.endswith(".png"):
#             card_name = card_file.split('_')[1].split('.')[0]
#             image_path = os.path.join(full_path, card_file)
#             card_image = pygame.image.load(image_path).convert_alpha()
#             scaled_card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
#             card_images[card_name] = scaled_card_image
#     return card_images

# # Function to display text on the screen
# def display_text(screen, text, position, color):
#     text_surface = FONT.render(text, True, color)
#     screen.blit(text_surface, position)

# # Main function to run the game
# def main():
#     # Initialize screen
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Diamonds Game")

#     # Initialize game variables
#     diamond_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']
#     player_deck = diamond_cards.copy()
#     computer_deck = diamond_cards.copy()
#     player_score = 0
#     computer_score = 0
#     round_number = 1
#     used_diamonds = []

#     running = True
#     # Main game loop
#     while diamond_cards:
        
#         screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         pygame.display.set_caption("Diamonds Game")

#         if not(diamond_cards):
#             break
#         current_diamond = generate_diamond_card(diamond_cards, used_diamonds)
#         # Clear the screen
#         screen.fill(WHITE)

#         diamond_images = load_card_images_suit("cards", "diamonds")
#         spade_images = load_card_images_suit("cards", "spades")
#         club_images = load_card_images_suit("cards", "clubs")
#         current_diamond_image = diamond_images.get(str(current_diamond), None)
        
#         if current_diamond_image:
#             screen.blit(current_diamond_image, (SCREEN_WIDTH // 2 - CARD_WIDTH // 2, SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2))

#         card_spacing = 2
#         # Display text asking for player's bid
#         display_text(screen, "Choose a card to bid:", (10, SCREEN_HEIGHT), BLACK)

        
#         for i, card in enumerate(player_deck):
#             card_image = spade_images.get(card, None)
#             if card_image:
#                 card_x = i * (CARD_WIDTH - card_spacing)  # Adjusted spacing between cards
#                 card_x = min(card_x, SCREEN_WIDTH - CARD_WIDTH)  # Ensure cards fit within screen width
#                 screen.blit(card_image, (card_x, SCREEN_HEIGHT - CARD_HEIGHT + 20))
                
#         for i, card in enumerate(computer_deck):
#             card_image = club_images.get(card, None)
#             if card_image:
#                 card_x = i * (CARD_WIDTH - card_spacing)  # Adjusted spacing between cards
#                 card_x = min(card_x, SCREEN_WIDTH - CARD_WIDTH)  # Ensure cards fit within screen width
#                 screen.blit(card_image, (card_x, SCREEN_HEIGHT - CARD_HEIGHT - 500))

        
#         display_text(screen, f"Player Score: {player_score}", (10, 10), BLACK)
#         display_text(screen, f"Computer Score: {computer_score}", (10, 50), BLACK)
#         pygame.display.flip()

#         while True:
#             event = pygame.event.wait()
#             if event.type == pygame.QUIT:
#                 running = False
#                 break
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Left mouse button
#                     mouse_x, mouse_y = pygame.mouse.get_pos()
#                     if SCREEN_HEIGHT - CARD_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
#                         selected_card_index = (mouse_x // CARD_WIDTH) % len(player_deck)
#                         selected_card = player_deck.pop(selected_card_index)

#                         computer_card = generate_computer_bid(computer_deck, used_diamonds)
#                         computer_deck.remove(computer_card)
                        
#                         # Determine winner of the round and update scores
#                         if CARD_VALUES[computer_card[0]] > CARD_VALUES[selected_card[0]]:
#                             computer_score += CARD_VALUES[current_diamond]
#                             text = "Computer Won this round"
#                         elif CARD_VALUES[computer_card[0]] == CARD_VALUES[selected_card[0]]:
#                             computer_score += CARD_VALUES[current_diamond]//2
#                             player_score += CARD_VALUES[current_diamond]//2
#                             text = "This round is a tie"
#                         else:
#                             player_score += CARD_VALUES[current_diamond]
#                             text = "You won this round"

#                         # Display computer's bid and round result
#                         display_text(screen, f"Computer's bid: {computer_card}   You bid: {selected_card}", (10, SCREEN_HEIGHT - 200), BLACK)
#                         display_text(screen, text, (10, SCREEN_HEIGHT - 250), BLACK)
#                         pygame.display.flip()
#                         pygame.time.delay(3000)
#                 break

#         # Update round number
#         round_number += 1

#     # Display final scores and winner
#     screen.fill(WHITE)
#     display_text(screen, f"Player Score: {player_score}", (10, 10), BLACK)
#     display_text(screen, f"Computer Score: {computer_score}", (10, 50), BLACK)

#     if player_score > computer_score:
#         text = "You won!"
#     elif player_score == computer_score:
#         text = "It's a tie!"
#     else:
#         text = "Computer won!"
    
#     display_text(screen, text, (300, 300), BLACK)

#     pygame.display.flip()
#     # Quit Pygame

#     while True:
#         event = pygame.event.wait()
#         if event.type == pygame.QUIT:    
#             pygame.quit()
#             break

# if __name__ == "__main__":
#     main()
