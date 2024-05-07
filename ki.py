import streamlit as st
from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
from requirements import pycryptodome

def rc4_encrypt(plaintext, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext)

def rc4_decrypt(ciphertext, key):
    cipher = ARC4.new(key)
    return cipher.decrypt(ciphertext)

def main():
    st.markdown(
        """
        <div style='text-align:center'>
            <img src='https://cdn-2.tstatic.net/tribunnews/foto/bank/images/sistem-manajemen-keamanan-informasi.jpg'>
        </div>
        """,
        
        unsafe_allow_html=True
    )

    st.title("Enkripsi Dekripsi Algoritma RC4 Test")
    st.markdown("---") 
    st.subheader("Created by: Elen Debina (227006043)")  
    plaintext = st.text_area("Masukan plainteks:")
    key = st.text_input("Masukan kunci:")
    num_bits = st.number_input("Jumlah Bit:", min_value=1, max_value=None, value=8)

    if st.button("Encrypt"):
        if plaintext and key:
            plaintext_bytes = plaintext.encode()
            key_bytes = key.encode()
            encrypted_text = rc4_encrypt(plaintext_bytes, key_bytes).hex()
            st.write("Encrypted text:", encrypted_text)

    if st.button("Decrypt"):
        if plaintext and key:
            ciphertext = bytes.fromhex(plaintext)
            key_bytes = key.encode()
            decrypted_text = rc4_decrypt(ciphertext, key_bytes).decode()
            st.write("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
