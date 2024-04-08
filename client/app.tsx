import React from 'react';
import ReactDOM from 'react-dom';
import {registerExtensions} from 'newsroom-core/assets/index';
import {CopyEmbedCodeBanner} from './copy-embed-code-banner';

registerExtensions({
    prepareWirePreview: (previewHtmlElement) => {
        for (const embedBlockHtmlElement of previewHtmlElement.querySelectorAll('.embed-block')) {

            const div = document.createElement('div');

            div.style.textAlign = 'center';

            ReactDOM.render(
                <CopyEmbedCodeBanner
                    onCopy={() => {
                        navigator.clipboard.writeText(embedBlockHtmlElement.innerHTML);
                    }}
                />,
                div,
            );

            const parent = embedBlockHtmlElement.parentElement;

            if (parent != null) {
                parent.insertBefore(div, embedBlockHtmlElement.nextSibling);
            }

        }

        return previewHtmlElement;

    }
});
