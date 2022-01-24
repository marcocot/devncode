---
layout: post
title: 'Javascript: flat & flatmap'
categories: ['javascript']
author: marcocot
draft: false
tags:
  - 'Javascript'
  - 'FP'
category: "Javascript"
description: 'Una delle novità di ES2019 è l’intruduzione (finalmente) di due nuovi metodi dell’oggetto Array: `flat()` e `flatMap()`'
date: '2019-12-09'
path: '/posts/javascript/es6-flat-and-flatmap'
---

Una delle novità di ES2019 è l’intruduzione (finalmente) di due nuovi metodi dell’oggetto Array: `flat()` e `flatMap()`

## Array.prototype.flat()

Il metodo `flat()` può appiattire un array multidimensionale:

```javascript
const myArray = [[1, 2], [3], [4, 5, 6]]
console.log(myArray.flat())

// => [1, 2, 3, 4, 5, 6];
```

`flat() può anche accettare un parametro opzionale, la profondità. Di default flat() scende solo al primo livello di profondità di un array:

```javascript
const myArray = [
  [1, 2, [3, 4]],
  [5, 6],
]
console.log(myArray.flat())

// => [1, 2, [3, 4], 5, 6]
```

Passando invece un valore di profondità maggiore, otteniamo questo:

```javascript
const myArray = [
  [1, 2, [3, 4]],
  [5, 6],
]
console.log(myArray.flat(2))

// => [1, 2, 3, 4, 5, 6]
```

In questo caso abbiamo scelto un valore di profondità di ricorsione di 2 poiché il sotto-array [3, 4] è ad un livello inferiore degli altri elementi di myArray.

Eventualmente possiamo anche usare Infinity per appiattire un array di profondità arbitraria:

```javascript
const myArray = [1, [3, [4, [5, 6, [7]]]]]

console.log(myArray.flat())
// => [1, 3, Array(2)];

console.log(myArray.flat(Infinity))
// => [1, 2, 3, 4, 5, 6, 7];
```

## Array.prototype.flatMap()

Il metodo flatMap è l’equivalente di eseguire map e successivamente flat(1) su un array:

```javascript
const myArray = [1, 2, 3, 4]
console.log(myArray.flatMap(x => [x * 2]))

// => [2, 4, 6, 8]
```

L’alternativa, senza flatMap() sarebbe:

```javascript
const myArray = [1, 2, 3, 4]

const result = myArray.map(x => [x * 2])
console.log(result)
// => [[2], [4], [6], [8]]

console.log(result.flat())
// => [2, 4, 6, 8]
```

flatMap() è, ad esempio, utile nel caso in cui abbiamo una array di stringhe da splittare in parole:

```javascript
const myString = ['Hello darkness', 'my old friend']
console.log(myString.flatMap(x => x.split(' ')))

// => ["Hello", "darkness", "my", "old", "friend"]
```