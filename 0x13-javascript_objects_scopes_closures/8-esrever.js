#!/usr/bin/node
/**
 * Write a function that returns the reversed version of a list:
 * Prototype: exports.esrever = function (list)
 * I'm not allow to use the built-in method reverse
 */
exports.esrever = function (list) {
  const newlist = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newlist[j] = list[i];
    j++;
  }
  return newlist;
};
