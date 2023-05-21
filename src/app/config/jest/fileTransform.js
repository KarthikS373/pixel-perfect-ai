'use strict';

const path = require('path');
const camelcase = require('camelcase');

module.exports = {
  process(src, filename) {
    const filenameOfAssets = JSON.stringify(path.basename(filename));

    if (filename.match(/\.svg$/)) {
      const filenameOfAssetInPascalCase = camelcase(path.parse(filename).name, {
        pascalCase: true,
      });
      
      const componentName = `Svg${filenameOfAssetInPascalCase}`;

      return `const React = require('react');
      module.exports = {
        __esModule: true,
        default: ${filenameOfAssets},
        ReactComponent: React.forwardRef(function ${componentName}(props, ref) {
          return {
            $$typeof: Symbol.for('react.element'),
            type: 'svg',
            ref: ref,
            key: null,
            props: Object.assign({}, props, {
              children: ${filenameOfAssets}
            })
          };
        }),
      };`;
    }

    return `module.exports = ${filenameOfAssets};`;
  },
};
