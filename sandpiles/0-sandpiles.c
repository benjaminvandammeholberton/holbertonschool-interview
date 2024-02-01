#include <stdio.h>
#include "sandpiles.h"

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 *
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * is_stable - Check if a sandpile is stable.
 *
 * @grid: The 3x3 grid representing the sandpile.
 *
 * Return: 1 if stable, 0 otherwise.
 */
int is_stable(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
			{
				return 1;
			}
		}
	}
	return 0;
}

/**
 * topple - Simulate the toppling process on a sandpile until
 * it becomes stable.
 *
 * @grid: The 3x3 grid representing the sandpile.
 */
void topple(int grid[3][3])
{
	int i, j;
	int temp_grid[3][3];

	while (is_stable(grid) == 1)
	{
		printf("=\n");
		print_grid(grid);
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				temp_grid[i][j] = 0;
			}
		}
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				if (grid[i][j] > 3)
				{
					temp_grid[i][j] -= 4;
					if (i - 1 >= 0)
						temp_grid[i - 1][j] += 1;

					if (i + 1 < 3)
						temp_grid[i + 1][j] += 1;

					if (j - 1 >= 0)
						temp_grid[i][j - 1] += 1;

					if (j + 1 < 3)
						temp_grid[i][j + 1] += 1;
				}
				temp_grid[i][j] += grid[i][j];
			}
		}
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				grid[i][j] = temp_grid[i][j];
			}
		}
	}
}

/**
 * sandpiles_sum - Add two sandpiles together and perform
 * the toppling process.
 *
 * @grid1: The first 3x3 grid representing a sandpile.
 * @grid2: The second 3x3 grid representing another sandpile.
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] = grid1[i][j] + grid2[i][j];
		}
	}
	topple(grid1);
}
