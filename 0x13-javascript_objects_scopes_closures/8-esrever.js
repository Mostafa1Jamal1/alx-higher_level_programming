#!/usr/bin/node

exports.esrever = function (list) {
  let newlist = [];
  for (const i of list) {
    newlist.unshift(i);
  }
  return newlist;
};
