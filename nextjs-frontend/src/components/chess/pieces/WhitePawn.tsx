import React from 'react'

const WhitePawn = (props: React.SVGProps<SVGSVGElement>) => {
    return (
        <div className="">
            <svg
                width="100px"
                height="100px"
                viewBox="0 0 76 76"
                xmlns="http://www.w3.org/2000/svg"
                xmlnsXlink="http://www.w3.org/1999/xlink"
                baseProfile="full"
                enableBackground="new 0 0 76.00 76.00"
                xmlSpace="preserve"
                {...props}
            >
                <path
                    fill="#FFFFFF"
                    fillOpacity={1}
                    strokeWidth={0.2}
                    strokeLinejoin="round"
                    d="M 24.9375,60.1667C 24.9375,53.0302 31.6667,53.8333 32.4475,42.75L 30.0833,42.75L 30.0833,41.1667L 33.6406,41.1667C 34.3703,37.9648 35.2292,33.8736 35.2292,28.5L 29.2917,28.5L 34.6833,25.8149C 33.3325,24.8043 32.4583,23.1917 32.4583,21.375C 32.4583,18.3144 34.9394,15.8333 38,15.8333C 41.0606,15.8333 43.5417,18.3144 43.5417,21.375C 43.5417,23.1917 42.6674,24.8043 41.3167,25.8149L 46.7083,28.5L 40.7708,28.5C 40.7708,33.8736 41.5941,37.9648 42.2676,41.1667L 45.9167,41.1667L 45.9167,42.75L 43.4298,42.75C 44.3333,53.8333 51.0625,53.0302 51.0625,60.1667L 24.9375,60.1667 Z "
                />
            </svg>
        </div>
    )
}
export default WhitePawn
