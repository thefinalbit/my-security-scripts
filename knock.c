/* ==================================================================
 * Study & Practice Script
 * Source: Public educational resources & technical tutorials
 * Note: Adapted for personal learning and concept analysis.
 * ==================================================================
 */

#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc == 2) {
        printf("Knock, Knock, %s\n", argv[1]);
    } else {
        fprintf(stderr, "Usage: %s <name>\n", argv[0]);
        return 1;
    }
    return 0;
}
