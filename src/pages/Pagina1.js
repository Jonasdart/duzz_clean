import React,{useEffect,useState} from 'react';
import { StyleSheet,
  Text,
  View,
  KeyboardAvoidingView,
  TextInput,
  TouchableOpacity,
  Image,
  Animated, 
  Keyboard,
  Alert
} from 'react-native';
import styles from '../styles/index';

export default function duzzclean() {
  
  
  clicou = ()=>{
    Alert.alert("Sucesso","Voce está conectado!")
  }

  const[offset]=useState(new Animated.ValueXY({x: 0,y:95}))
  const[opacity]=useState(new Animated.Value(0))
  const[logo]= useState(new Animated.ValueXY({x:280 , y:179}));


  useEffect(()=>{
    keyboardDidShowListener = Keyboard.addListener('keyboardDidShow',keyboardDidShow);
    keyboardDidShowListener = Keyboard.addListener('keyboardDidHide',keyboardDidHide);

    Animated.parallel([
    Animated.spring(offset.y,{
      toValue:0,
      speed: 3,
      bounciness:20,
      useNativeDriver: false 

        }),
    Animated.timing(opacity,{
      toValue:1,
      duration:300,
      useNativeDriver: false 

    })

  ]).start();
  },[]);
  function keyboardDidShow(){
     

    Animated.parallel([
      Animated.timing(logo.x,{
        toValue:125,
        duration:100,
        useNativeDriver: false 
      }),
  Animated.timing(logo.y,{
        toValue:80,
        duration:100,
        useNativeDriver: false 
      })
      
    ]).start();
  }
  function keyboardDidHide(){
    Animated.parallel([
      Animated.timing(logo.x,{
        toValue:227, 
        duration:100,
        useNativeDriver: false 
      }),
  Animated.timing(logo.y,{
        toValue:146,
        duration:100,
        useNativeDriver: false         
      })
    ]).start();
  }
  return (
    <KeyboardAvoidingView style={styles.background}>

               <View style={styles.containerLogo}>
                <Animated.Image 
                style={{
                  width:logo.x,
                  height:logo.y,
                }}
                source={require('../components/assets/logo.png')}/>
              </View> 
                <Animated.View 
                style={[
                  styles.container,
                  {
                    opacity:opacity,
                    transform: [
                      {translateY:offset.y}
                    ]
                  }
                ]}>
                      <TextInput 
                      style={styles.input}
                      placeholder="Digite seu email"
                      autoCorrect={false}
                      onChangeText={()=>{}}>
                      </TextInput>

                      <TextInput 
                      style={styles.input}           
                      secureTextEntry={true}           
                      placeholder="Digite sua senha" 
                      autoCorrect={false} 
                      onChangeText={()=>{}}>
                      </TextInput>
                    <TouchableOpacity
                     style={styles.btnSubmit} 
                    onPress={()=>{this.props.navigation.navigate('Home')}}
                    >
                      <Text style={styles.submitText}>Acessar</Text>
                      
                    </TouchableOpacity>

                    <TouchableOpacity style={styles.btnRegister}>
                      <Text style={styles.registerText}>Criar Conta gratuita</Text>
                    </TouchableOpacity>
                  </Animated.View>
        </KeyboardAvoidingView>
    );
}
