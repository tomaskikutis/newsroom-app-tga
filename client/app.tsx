import React from 'react';
import ReactDOM from 'react-dom';
import {registerExtensions} from 'newsroom-core/assets/index';
import {CopyEmbedCodeBanner} from './copy-embed-code-banner';

registerExtensions({
    prepareWirePreview: (previewHtmlElement, article) => {
        for (const embedBlockHtmlElement of previewHtmlElement.querySelectorAll('.embed-block')) {
            const embeddedArticleId = embedBlockHtmlElement.getAttribute('data-association-key');

            if (embeddedArticleId == null) {
                continue;
            }

            const embeddedArticle = article.associations?.[embeddedArticleId];

            if (embeddedArticle == null) {
                continue;
            }

            const licenseName = (embeddedArticle.subject ?? []).find(({scheme}) => scheme === 'licence_type')?.name;

            if (licenseName == null) {
                continue;
            }

            const div = document.createElement('div');

            div.style.textAlign = 'center';

            ReactDOM.render(
                <CopyEmbedCodeBanner
                    license={licenseName}
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
