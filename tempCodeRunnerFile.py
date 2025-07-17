      snake_length += 1

            if (snake_x >= screen_width or snake_x < 0 or
                snake_y >= screen_height or snake_y < 0):
                game_over = True

            if len(snake_blocks) == 3 and not continue_game:
                # If the game is not set to continue, only then end the game
                game_over = True
                try: