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