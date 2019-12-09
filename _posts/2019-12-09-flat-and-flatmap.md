---
layout: post
title: "Javascript: flat & flatmap"
categories: ["javascript"]
tags: ["js", "fp"]
author: marcocot
---

Una delle novità di ES2019 è l’intruduzione (finalmente) di due nuovi metodi dell’oggetto Array: `flat()` e `flatMap()`

## Array.prototype.flat()

Il metodo `flat()` può appiattire un array multidimensionale:

{% highlight js %}
const myArray = [[1, 2], [3], [4, 5, 6]];
console.log(myArray.flat());

// => [1, 2, 3, 4, 5, 6];
{% endhighlight %}

`flat() può anche accettare un parametro opzionale, la profondità. Di default flat() scende solo al primo livello di profondità di un array:

{% highlight js %}
const myArray = [[1, 2, [3, 4]], [5, 6]];
console.log(myArray.flat());

// => [1, 2, [3, 4], 5, 6]
{% endhighlight %}

Passando invece un valore di profondità maggiore, otteniamo questo:

{% highlight js %}
const myArray = [[1, 2, [3, 4]], [5, 6]];
console.log(myArray.flat(2));

// => [1, 2, 3, 4, 5, 6]
{% endhighlight %}

In questo caso abbiamo scelto un valore di profondità di ricorsione di 2 poiché il sotto-array [3, 4] è ad un livello inferiore degli altri elementi di myArray.

Eventualmente possiamo anche usare Infinity per appiattire un array di profondità arbitraria:

{% highlight js %}
const myArray = [1, [3, [4, [5, 6, [7]]]]];

console.log(myArray.flat());
// => [1, 3, Array(2)];

console.log(myArray.flat(Infinity));
// => [1, 2, 3, 4, 5, 6, 7];
{% endhighlight %}

## Array.prototype.flatMap()

Il metodo flatMap è l’equivalente di eseguire map e successivamente flat(1) su un array:

{% highlight js %}
const myArray = [1, 2, 3, 4];
console.log(myArray.flatMap(x => [x * 2]));

// => [2, 4, 6, 8]
{% endhighlight %}

L’alternativa, senza flatMap() sarebbe:

{% highlight js %}
const myArray = [1, 2, 3, 4];

const result = myArray.map(x => [x * 2]);
console.log(result);
// => [[2], [4], [6], [8]]

console.log(result.flat());
// =>  [2, 4, 6, 8]
{% endhighlight %}

flatMap() è, ad esempio, utile nel caso in cui abbiamo una array di stringhe da splittare in parole:

{% highlight js %}
const myString = ["Hello darkness", "my old friend"];
console.log(myString.flatMap(x => x.split(" ")));

// => ["Hello", "darkness", "my", "old", "friend"]
{% endhighlight %}
