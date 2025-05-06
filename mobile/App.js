import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import LoginScreen from './screens/LoginScreen';
import SignupScreen from './screens/SignupScreen';
import MapScreen from './screens/MapScreen';

const AuthStack = createNativeStackNavigator();
const AppStack  = createNativeStackNavigator();

export default function App() {
  const [token, setToken] = useState(null);

  return (
    <NavigationContainer>
      {token == null ? (
        <AuthStack.Navigator>
          <AuthStack.Screen name="Login">
            {props => <LoginScreen {...props} onLogin={setToken} />}
          </AuthStack.Screen>
          <AuthStack.Screen name="Sign Up">
            {props => <SignupScreen {...props} onSignup={setToken} />}
          </AuthStack.Screen>
        </AuthStack.Navigator>
      ) : (
        <AppStack.Navigator>
          <AppStack.Screen name="Map">
            {props => <MapScreen {...props} accessToken={token} />}
          </AppStack.Screen>
          {/* Add CirclesList, Profile, etc. here */}
        </AppStack.Navigator>
      )}
    </NavigationContainer>
  );
}
