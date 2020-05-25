#ifndef BMHALG_H
#define BMHALG_H

#include <string>

/*! \brief The function of image search in a line.
 *
 *  \param str  Line.
 *  \param img  Image.
 *
 *  \return The index of the first entry img into str, if found.
 *          str length, otherwise.
 */
size_t algBMH(std::string str, std::string img);

#endif // BMHALG_H