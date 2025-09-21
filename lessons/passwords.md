---
layout: page
title:  Passwords
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}
</style>

# Passwords
{: .no_toc}

![Comic: My Password is Password123](https://cdn.shopify.com/s/files/1/0077/2554/7593/files/important-password-the-introverted-attorney-lawyer-comic_600x600.png?v=1614183796)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How Strong Is Your Password?
Ahmad was beside Omar when he was typing his password. Ahmad noticed that Omar typed **6 lowercase letters**, but couldn't tell which ones. He wants to guess Omar's password by trying all possible passwords made of 6 lowercase letters. How many such passwords are there?

Since there are 26 possible lowercase letters, there are:

$$26^6 = 308,915,776\approx 309 \textrm{ million}$$

different possible passwords made of 6 lowercase letters. This might sound safe. After all, any website is likely to lock Ahmad out if he provides an incorrect password a few times! 

Imagine if the password database of Omar's website was leaked and Ahmad had access to it ([this could happen even with top websites!](https://www.mcafee.com/blogs/internet-security/26-billion-records-released-the-mother-of-all-breaches/)). Typically, websites store passwords **encrypted**. Hence, Omar's password should still be unreadable by Ahmad. However, Ahmad now has an easy way to crack Omar's password!

Knowing Omar's encrypted password, Ahmad can try to encrypt the `308,915,776` possible passwords and see if any matches Omar's encrypted password. This can be done on a laptop in a matter of hours, and on a stronger computer with multiple GPUs in a matter of seconds or less!

Most websites currently require passwords to be at least 8 characters long, and to contain a combination of uppercase letters, lowercase letters, numbers, and special characters. How secure does this make the password? 

{: .example-title }
> Do The Math
>
> If the password has 8 lowercase characters, the number of possible passwords is:
>
> $$26^8 = 208,827,064,576\approx 209 \textrm{ billion}$$
> 
> If the password has also uppercase characters, the number is:
>
> $$(26 + 26)^8 = 53,459,729,000,000\approx 53 \textrm{ trillion}$$
>
> If it also has numbers:
>
> $$(26 + 26 + 10)^8 = 218,340,110,000,000\approx 218 \textrm{ trillion}$$
>
> Assume also that there is also one of 32 special characters:
>
> $$(26 + 26 + 10 + 32)^8 = 6,095,689,400,000,000\approx 6 \textrm{ quadrillion}$$

Adding such requirements makes it practically impossible even for the fastest computers to crack the password.

{: .highlight-title }
> 🔗 **LINK**
>
> The following website provides estimates for how long it takes to crack your password!
> [https://bitwarden.com/password-strength/](https://bitwarden.com/password-strength/){:target="_blank"}

Are there other factors (beside the number and type of characters used) that can make a password unsafe? Yes, there are strings that are commonly used in passwords (e.g., `password`, `1234`, etc.) which crackers check along with certain variations of them. Hence, the password `Password_1` is unsafe although it is $$10$$ characters long and contains lowercase letters, an uppercase letter, a number, and a special character.

{: .important-title }
> 📖 Definitions
>
> **A Dictionary Attack** is an attempt to guess the password based on a predefined list of strings. The list can contain English words (hence the name _dictionary_), common strings found in passwords, or actual passwords collected from previous breaches. The attacker typically uses a software to create variations of the strings in the dictionary (e.g., appending a number or a special character).
>
> **A Rainbow Table** is a dictionary, where the strings (e.g., the common passwords) are not stored in plaintext, but are stored after being encrypted using one of the encryption methods commonly used for passwords. This can speed up the dictionary attack, as the the attacker only has to search for the encrypted string, instead of encrypting it before searching.

{: .highlight-title }
> 🔗 **LINK**
>
> Watch a live demo of dictionary attacks:
> [Password Cracking on Computerphile](https://www.youtube.com/watch?v=7U-RbOKanYs&ab_channel=Computerphile){:target="_blank"}


The following function checks if a given password is safe. It checks the number and type of characters used and whether the password matches a common password in a given dictionary. This is not safe enough against sophisticated dictionary attacks (more practice on this in the exercises!).

{% include expandable-code.html
   title="Python Code"
   id="is-safe"
   language="python"
   file='code/is_safe.py'
%}

{: .highlight-title }
> 💡 **NOTE**
>
> The above code is not **_pythonic_**. Use your favorite GenAI tool to see examples of pythonic versions. Ask for the use of `any` in your prompt or for the use of **regulat expressions**. We did not cover these features, so don't worry about understanding every bit of detail.


## Random Password Generation
Let's write a program that generates a random secure password. This is a useful task performed by password managers.

{% include expandable-code.html
   title="Python Code"
   id="random-password"
   language="python"
   file='code/rand_pass.py'
%}

While the generated passwords are secure, they are very hard to remember. Another way is to concatenate 4 words from the English dictionary. While the password would not be made only of lowercase letters, the password would still be long enough to be secure.

{% include expandable-code.html
   title="Python Code"
   id="xkcd"
   language="python"
   file='code/rand_pass2.py'
%}

You will practice in the exercises creating variants of this program that make the generated password even more secure.

{: .highlight-title }
> 💡 **INFO**
>
> This idea is often referred to as `xkcd` password generation, as it is inspired by a famous [xkcd cartoon](https://xkcd.com/936/). There is even a python library named `xkcdpass` that you can install and import to generate passwords this way! (don't be afraid to read the [documentation](https://pypi.org/project/xkcdpass/)!)


## Storing Passwords

As we have mentioned above, no sane application stores its users' passwords in plaintext. Not even the application administrators should be able to read such sensitive information. Let alone the possibility of hackers getting unauthorized access to the files storing these passwords. The minimum that should be done is to store the passwords in some encrypted format.

How can the application authorize users if they don't know their passwords?

The answer is easy. If the application stores an encrypted version of the password at signup, when the user requests to login using a password, this password is encrypted and compared to the encrypted one stored before.

For this procedure to be secure, a **one-way** encryption method must be used. I.e., given the password, it should be easy to know its encrypted version. However, given the encrypted version, there should be no practical way for knowing the original password. This is often referred to as **hashing**.

{: .important-title }
> 📖 Definition
>
> **A Cryptographic Hash Function** $$f(p)$$ is a function that receives a string (e.g., a password) and returns a new string, with the following conditions:
> 1. $$f(p)$$ always returns the same string if $$p$$ did not change.
> 2. If $$p$$ changes, then $$f(p)$$ must change with extremely high probability.
> 3. Given $$f(p)$$ there should be no practical way for knowing the value of $$p$$.
> 4. Finding $$p_1 \neq p_2$$ such that $$f(p_1) = f(p_2)$$ should be practically impossible.

The following code snippet shows how to use the [`hashlib`](https://docs.python.org/3/library/hashlib.html) library to generate a _hashed_ version of a password. This piece of code uses a hash function named SHA256.

{% include expandable-code.html
   title="Python Code"
   id="hashlib"
   language="python"
   file='code/hashlib_example.py'
%}

While storing the hashed version of a password is good, it is still not very secure. The reason is that by looking at a leaked file of hashed passwords one can tell which users have the same password. This means that compromising one account leads to compromising all the other accounts using the same password. For this reason, applications typically add a **salt** to every password before hashing it. A salt is an extra random string (different for different users) added to the password before hashing it and stored alongside the password (often in plaintext). This way, if two users use the same password, their hashes will look different, because their salts are different.

The following program shows how salting can be used.

{% include expandable-code.html
   title="Python Code"
   id="salt"
   language="python"
   file='code/salt.py'
%}

The above procedure is still not very secure. The problem is that SHA256 is a very fast hashing function. While this might sound good, it is bad for security reasons. A slow hash function makes the job of a hacker harder, because the time needed for a bruteforce attack does not only depend on how many passwords will be tested, but also how long it takes to test a single password! Therefore, it advisable to use libraries like [`bcrypt`](https://pypi.org/project/bcrypt/) and [`scrypt`](https://pypi.org/project/scrypt/), which provide slow (i.e., more secure) hashing algorithms.

{: .highlight-title }
> 🔗 **LINK**
>
> The following video summarizes nicely how passwords should be stored:
> [Studying With Alex: Password Storage Tier List](https://www.youtube.com/watch?v=qgpsIBLvrGY&ab_channel=StudyingWithAlex)

## Exercises (REMOVE BEFORE PUBLISHING)

1. Write test cases for function X
2. Implement a dictionary attack that does a minor variation to the words in the dictionary.
3. Write a python program that generates a random password by concatenating 5 words from a dictionary.
    - They should be unique
4. Modify the xkcd program:
    - Capitalize every word
    - Add random special_chars or numbers between words
    - Guarantee uniqueness
    - length of words >= 3
    - min_number of words used, max_number of words used
5. Write a user-login manager? https://www.youtube.com/watch?v=MYYWnRDP8Q0&ab_channel=WJPearce
6. Something about prompting and generation using AI.
7. Something about code reading.
8. getpass ?