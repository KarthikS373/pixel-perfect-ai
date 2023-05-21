'use strict';
const { createHash } = require('crypto');

module.exports = env => {
  const md5Hash = createmd5Hash('md5');
  md5Hash.update(JSON.stringify(env));

  return md5Hash.digest('hex');
};
