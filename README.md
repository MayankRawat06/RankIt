# RankIt

## What is TOPSIS?

**T**echnique for **O**rder **P**reference by **S**imilarity to **I**deal **S**olution
(TOPSIS) originated in the 1980s as a multi-criteria decision making method.
TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution,
and greatest distance from the negative-ideal solution.

<br>

Topsis-Mayank-102016012 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Topsis-Mayank-102016012.

```
>> pip install Topsis-Mayank-102016012
```

## Usage

Enter csv filename followed by _.csv_ extension, then enter the _weights_ vector with vector values separated by commas, followed by the _impacts_ vector with comma separated signs _(+,-)_, further followed by the filename having _.csv_ extension to store result

```
>> topsis data.csv "1,1,1,1" "+,-,+,+" res.csv
```

or vectors can be entered without " "

```
>> topsis data.csv 1,1,1,1 +,-,+,+ res.csv
```

But the second representation does not provide for inadvertent spaces between vector values. So, if the input string contains spaces, make sure to enclose it between double quotes _(" ")_.

To view usage **help**, use

```
topsis /h
```

## Example

#### data.csv

The decision matrix should be constructed with each row representing a Model alternative, and each column representing a criterion like Accuracy, R<sup>2</sup>, Root Mean Squared Error, Correlation, and many more.

| Model | Correlation | R<sup>2</sup> | RMSE | Accuracy |
| ----- | ----------- | ------------- | ---- | -------- |
| M1    | 0.79        | 0.62          | 1.25 | 60.89    |
| M2    | 0.66        | 0.44          | 2.89 | 63.07    |
| M3    | 0.56        | 0.31          | 1.57 | 62.87    |
| M4    | 0.82        | 0.67          | 2.68 | 70.19    |
| M5    | 0.75        | 0.56          | 1.3  | 80.39    |

Weights (`weights`) is not already normalised will be normalised later in the code.

Information of benefit positive(+) or negative(-) impact criteria should be provided in `impacts`.

### Input:

```python
topsis data.csv "0.25,0.25,0.25,0.25" "+,+,-,+" result.csv
```

<br>

## Output file (result.csv)

| Model | Correlation | R<sup>2</sup> | RMSE | Accuracy | Score  | Rank |
| ----- | ----------- | ------------- | ---- | -------- | ------ | ---- |
| M1    | 0.79        | 0.62          | 1.25 | 60.89    | 0.7722 | 2    |
| M2    | 0.66        | 0.44          | 2.89 | 63.07    | 0.2255 | 5    |
| M3    | 0.56        | 0.31          | 1.57 | 62.87    | 0.4388 | 4    |
| M4    | 0.82        | 0.67          | 2.68 | 70.19    | 0.5238 | 3    |
| M5    | 0.75        | 0.56          | 1.3  | 80.39    | 0.8113 | 1    |

<br>
The output file contains columns of input file along with two additional columns having **Score** and **Rank**

## Other notes

- The first column and first row are removed by the library before processing, in attempt to remove indices and headers. So make sure the csv follows the format as shown in data.csv.
- Make sure the csv does not contain categorical values

## License

[MIT](https://choosealicense.com/licenses/mit/)
