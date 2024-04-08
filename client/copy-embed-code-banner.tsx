import React, {useState} from 'react';
import {exposed} from 'newsroom-core/assets/index';

const bannerStyle: React.CSSProperties = {
    display: 'flex',
    gap: 16,
    alignItems: 'center',
    background: 'var(--color-background--muted)',
    padding: 'var(--space--1-5)',
    border: '1px solid var(--color-line--light)',
    borderRadius: 'var(--border-radius--m)',
    color: 'var(--color-text--muted)',
    marginTop: 16,
};

const textStyle: React.CSSProperties = {
    margin: 0,
    textAlign: 'justify',
    lineHeight: 1.2,
    fontSize: 'var(--text-size--medium)',
}

const {Button} = exposed.ui;
const {gettext} = exposed.locale;

interface IProps {
    onCopy(): void;
    license: string;
}

export function CopyEmbedCodeBanner(props: IProps) {
    const initialLabel = gettext('copy');
    const [label, setLabel] = useState(initialLabel);

    return (
        <div style={bannerStyle}>
            <div>
                <img src="/theme/360-Logo.png" style={{width: '100%', maxHeight: 32}} />
            </div>

            <p style={textStyle}>
                {gettext('Copy this into your own story. Available under {{x}} license.', {x: props.license})}
            </p>

            <Button
                text={label}
                size="small"
                onClick={() => {
                    props.onCopy();

                    setLabel(gettext('Copied!'));

                    setTimeout(() => {
                        setLabel(initialLabel);
                    }, 1000);
                }}
            />
        </div>
    );
}
