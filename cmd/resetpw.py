import sys
from db import Session, User, Auth

def main(email, lifetime):
	with Session() as sess:
		user = sess.query(User).filter(User.email == email).one_or_none()
		if user is None:
			print("User not found: '{}'".format(email))
			return
		token = Auth.CreateToken(email, lifetime = lifetime)
	print("Reset link:")
	print('http://sxsurimessenger.ml:8080/reset{}'.format(token))

if __name__ == '__main__':
	main(sys.argv[1], int(sys.argv[2]))
