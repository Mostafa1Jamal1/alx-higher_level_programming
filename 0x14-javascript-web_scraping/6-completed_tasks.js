#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (!err) {
    const TaskList = JSON.parse(body);
    const result = {};
    for (const i in TaskList) {
      const task = TaskList[i];
      if (!(String(task.userId) in result)) {
        result[String(task.userId)] = 0;
      }
      if (task.completed) {
        result[String(task.userId)] += 1;
      }
    }
    console.log(result);
  }
});
