#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (!err) {
    const TaskList = JSON.parse(body);
    const result = {};
    for (const task of TaskList) {
      const userId = String(task.userId);
      if (task.completed) {
        if (!(userId in result)) {
          result[userId] = 0;
        }
        result[userId] += 1;
      }
    }
    console.log(result);
  }
});
