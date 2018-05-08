#include<bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    
    
    ll q;
    cin>>q;
    while(q--){
        ll n;
        cin>>n;
    ll a[10000];
    a[1]=1;
    a[2]=1;
    a[3]=2;
    ll i=0;
    ll sm = 2;
    for(i=4;i<100;i++){
        
        a[i]=a[i-1]+a[i-2];
        if(a[i]>n)
            break;
      // cout<<a[i]<<endl;
        if(a[i]%2==0)
            sm+=a[i];
        
    }
    //cout<<i;
        cout<<sm<<endl;
    }
    
    return 0;
}

