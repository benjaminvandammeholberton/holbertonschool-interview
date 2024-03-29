#include "menger.h"

/**
 * menger - Draws a 2D Menger Sponge
 * @level: Level of the Menger Sponge to draw
 */
void menger(int level)
{
	int size, row, col, step;

	if (level < 0)
		return;

	size = pow(3, level);
	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
		{
			for (step = size / 3; step; step /= 3)
			{
				if ((row % (step * 3)) / step == 1 && (col % (step * 3)) / step == 1)
				{
					printf(" ");
					break;
				}
			}
			if (!step)
				printf("#");
		}
		printf("\n");
	}
}
