
// This means that we aren't allowed to use hooks inside loops, conditions or nested functions.
// We should never call a hook conditionally.
import React, { useState } from 'react';

export default function App() {
    const [count, setCount] = useState(0);

    if (count > 0) {
        return <h1>Count is greater than 0</h1>;
    }

    // ⛔️ React Hook "useState" is called conditionally.
    //React Hooks must be called in the exact same order
    // in every component render. Did you accidentally call
    // a React Hook after an early return?
    const [message, setMessage] = useState('');

    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}

import React, { useState } from 'react';

export default function App() {
    const [count, setCount] = useState(0);

    if (count === 0) {
        // ⛔️ React Hook "useState" is called conditionally.
        // React Hooks must be called in the exact same order in every component render.
        const [message, setMessage] = useState('');
    }


    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}

