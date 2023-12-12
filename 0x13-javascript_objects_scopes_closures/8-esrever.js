#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  for (const i of list) {
    newlist.unshift(i);
  }
  return newlist;
};
