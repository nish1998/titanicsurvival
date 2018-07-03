# titanicsurvival
RestAPI with flask using RandomForestClassifier

## link https://titanicsurvival.herokuapp.com/

### Use postman to check with post request to the link https://titanicsurvival.herokuapp.com/predict:

{
	"x":1,
	"y":0,
	"z":1,
	"l":70,
	"m":2,
	"n":2,
	"o":70
}

x=1 if female and x=0 if male

y=1 if male and y=0 if female

z=passenger class(1/2/3)

l=age

m=siblings

n=parents/children

o=fare


### Result: 1-survive 0-survivn't
