import React, { useState } from 'react';
import { View, TextInput, Button, Alert } from 'react-native';

export default function LoginScreen ({ onLogin}) {
    const [email, setEmail]         = useState('');
    const [password, setPassword]   = useState('');

    const login = async () => {
        const res = await fetch('http://http://127.0.0.1:8000//api/auth/login/', {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({email, password}),

        });
        if (!res.ok) return Alert.alert('Login failed');
        const { access } = await res.json();
        onLogin(access);
    };

    return (
        <View style= {{padding:16}}>
            <TextInput placeholder="Email" onChange Text={setEmail} value={email} autoCapitalize="none" />
            <TextInput placeholder="Password" onChangeText={setPassword} value={password} secureTextEntry />
            <Button title="Log In" onPress={login} />
            </View>
    );
}